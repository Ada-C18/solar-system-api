from os import abort
from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

solar_system_bp = Blueprint(
    "solar_system_bp", __name__, url_prefix="/solar-system"
    )

def verify_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))
    
    planet = Planet.query.get(planet_id)
    
    if not planet:
        abort(make_response(
        {"message":f"planet {planet_id} not found"}, 404
        ))
    
    return planet

@solar_system_bp.route("", methods=["GET"])
def read_all_planets():
    planets_response = []
    planets = Planet.query.all()
    for planet in planets:
        planets_response.append(planet.make_a_dict())
    return jsonify(planets_response)

@solar_system_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = verify_planet(planet_id)
    return jsonify(planet.make_a_dict())

