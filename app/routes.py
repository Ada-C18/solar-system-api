from flask import Blueprint, jsonify, abort, make_response

solar_system_bp = Blueprint(
    "solar_system_bp", __name__, url_prefix="/solar-system"
    )

@solar_system_bp.route("", methods=["GET"])
def handle_planets():
    planets_response = []
    for planet in solar_system:
        planets_response.append(planet.make_a_dict())
    return jsonify(planets_response)

@solar_system_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planet = verify_planet(planet_id)

    return jsonify(planet.make_a_dict())

def verify_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))
    
    for planet in solar_system:
        if planet.id == planet_id:
            return planet
    
    return abort(make_response(
        {"message":f"planet {planet_id} not found"}, 404
        ))

