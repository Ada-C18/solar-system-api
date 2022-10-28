from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet

# planets = [
#     Planet(1, "Mercury", "solid", 0),
#     Planet(2, "Venus", "bright and volcanic", 0),
#     Planet(3, "Earth", "half and half", 1)
# ]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"], description=request_body["description"], moons=request_body["moons"])
    db.session.add(new_planet)
    db.session.commit()
    return make_response(f"Planet {new_planet.name} has been created successfully", 201)

@planets_bp.route("", methods=["GET"])
def read_all_planets():
    planets = Planet.query.all()
    planets_response = [planet.to_dict() for planet in planets]
    return jsonify(planets_response)

# @planets_bp.route("", methods=["GET"])
# def planets_endpoint():
#     response = [planet.to_json() for planet in planets]
    
#     return jsonify(response)

# @planets_bp.route("/<planet_id>", methods=["GET"])
# def planet_endpoint(planet_id):
#     planet = validate_planet(planet_id)

#     return jsonify(planet.to_json())

# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"message":f"planet {planet_id} invalid"}, 400))
    
#     for planet in planets:
#         if planet.id == planet_id:
#             return planet

#     abort(make_response({"message":f"planet {planet_id} not found"}, 404))