from app import db
from app.models.planet import Planet
from flask import Blueprint
from flask import request, make_response, jsonify


planet_bp = Blueprint("planet", __name__, url_prefix="/planets")


@planet_bp.route("/", methods=["GET", "POST"])
def handle_all_planets():
    if request.method == "GET":
        name_query = request.args.get("name")
        if name_query:
            planets_result = Planet.query.filter_by(name=name_query)
        else:
            planets_result = Planet.query.all()
        return jsonify([p.planet_dict() for p in planets_result]), 200
    elif request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(
            name=request_body["name"],
            description=request_body["description"],
            mass=request_body["mass"],
        )
        db.session.add(new_planet)
        db.session.commit()
        return {"success": f"Planet {new_planet.name} is now in orbit"}, 201


@planet_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE"])
def handle_planet(planet_id):
    if not planet_id.isnumeric():
        return {"error": f"Planet #{planet_id} Invalid id"}, 400

    planet = Planet.query.get(planet_id)
    if not planet:
        return {"error": f"Planet #{planet_id} No planet found"}, 404

    elif request.method == "GET":
        return planet.planet_dict()
    elif request.method == "PUT":
        form_data = request.get_json()
        planet.name = form_data["name"]
        planet.description = form_data["description"]
        planet.mass = form_data["mass"]
        db.session.commit()
        return {"success": f"Planet #{planet_id} successfully updated"}, 200
    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()
        return {"success": f"Planet #{planet_id} successfully deleted"}, 200

