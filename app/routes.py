from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

#     for planet in planets:
#         if planet.id == planet_id:
#             return planet

#     abort(make_response({"message":f"planet {planet_id} not found"}, 404))

bp = Blueprint("planets", __name__, url_prefix = "/planets")

@bp.route("", methods=["GET"])
def read_all_planets():
    planets = Planet.query.all()
    planet_response = [planet.to_dict() for planet in planets]
    return jsonify(planet_response)

@bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name=request_body["name"],
        description=request_body["description"],
        moons=request_body["moons"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

# @bp.route("/<planet_id>", methods=["GET"])
# def handle_one_planet(planet_id):
#     planet = validate_planet(planet_id)
    
#     return jsonify(planet.to_planet_dict())
