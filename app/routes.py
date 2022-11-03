from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

planet_bp = Blueprint("planet", __name__, url_prefix="/planets")

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"{planet_id} is not a valid planet id"}, 400))

    planet = Planet.query.get(planet_id)
    if not planet:
        abort(make_response({"message": f"{planet_id} not found"}, 404))
    
    return planet

@planet_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planet = validate_planet(planet_id)

    return jsonify(planet.to_dict()), 200

@planet_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planet_bp.route("", methods=["GET"])
def handle_planets():
    name_query = request.args.get("name")
    size_query = request.args.get("size")

    planet_query = Planet.query

    if name_query:
        planet_query = planet_query.filter_by(name=name_query) 

    if size_query:
        planet_query = planet_query.filter_by(size=size_query)

    planets = planet_query.all()
    planets_response = [planet.to_dict() for planet in planets]
    return jsonify(planets_response)

# update planet
@planet_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.size = request_body["size"]
    planet.description = request_body["description"]

    db.session.commit()

    return make_response(f"Planet {planet.id} successfully updated"), 200

# delete planet
@planet_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet {planet.id} successfully deleted"), 200