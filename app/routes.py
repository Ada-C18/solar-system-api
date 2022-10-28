from flask import Blueprint, jsonify, abort, make_response

class Planet:
    def __init__(self, id, name, description, color):
        self.id = id
        self.name = name
        self.description = description
        self.color = color

PLANETS = [
            Planet(1, "Pluto", "no longer a planet", "light blue"),
            Planet(2, "Mercury", "smallest planet out of the 8", "dark gray"),
            Planet(3, "Mars", "closest resemblance to Earth", "red")
        ]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

# HELPER FUNCTIONS
def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"Planet {planet_id} invalid"}, 400))

    for planet in PLANETS:
        if planet.id == planet_id:
            return planet

    abort(make_response({"message": f"Planet {planet_id} not found"}, 404))

def planet_dict(planet):
    return {
        "id": planet.id, 
        "name": planet.name, 
        "description": planet.description,
        "color": planet.color
    }

# ROUTES
@planets_bp.route("", methods=["GET"])
def get_all_planets():
    planets_response = []

    for planet in PLANETS:
        planets_response.append(planet_dict(planet))

    return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)
    
    return planet_dict(planet)