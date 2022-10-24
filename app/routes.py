from flask import Blueprint, jsonify, abort, make_response

class Planet:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

solar_system = [
    Planet(1, "Mercury", "smallest planet"),
    Planet(2, "Venus", "hottest planet"),
    Planet(3, "Earth", "only planet known to harbor intelligent life"),
    Planet(4, "Mars", "most likely planet to terraform"),
    Planet(5, "Jupiter", "largest planet"),
    Planet(6, "Saturn", "only planet with a ring system"),
    Planet(7, "Uranus", "only planet with an almost vertical equator"),
    Planet(8, "Neptune", "coldest planet"),
    Planet(9, "Pluto", "only planet to be disowned fromt the Solar System")
]

solar_system_bp = Blueprint(
    "solar_system_bp", __name__, url_prefix="/solar-system"
    )

@solar_system_bp.route("", methods=["GET"])
def handle_planets():
    planets_response = []
    for planet in solar_system:
        planets_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description
            }
        )
    return jsonify(planets_response)

@solar_system_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planet = verify_planet(planet_id)

    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
    }

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

