from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, abort, request

bp = Blueprint("planets", __name__, url_prefix="/planets")

# Helper function
def  validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"planet {planet_id} invalid"}, 400))

    planet = Planet.query.get(planet_id)
    if not planet:
        abort(make_response({"message": f"planet {planet_id} not found"}, 404))
    return planet


@bp.route("", methods=["GET"])
def get_all_planets():
    planets = Planet.query.all() # returns a list of planet instances
    planets_response = [planet.to_dict() for planet in planets]
    return jsonify(planets_response), 200


@bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planet = validate_planet(planet_id)
    return planet.to_dict(), 200


@bp.route("", methods = ["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name=request_body["name"],
        size=request_body["size"],
        description=request_body["description"]
        )
    db.session.add(new_planet)
    db.session.commit()
    return make_response(f"Planet {new_planet.name} was successfully created", 201)






