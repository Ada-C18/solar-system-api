from flask import Blueprint, jsonify, abort, make_response

"""
1. Define a Planet class with the attributes id, name, and description, 
and one additional attribute
2. Create the following endpoint(s), with similar functionality presented in the
Hello Books API.
"""


class Planet:
    def __init__(self, id, name, description, moon):
        self.id = id
        self.name = name
        self.description = description
        self.moon = moon

PLANETS = [
    Planet(1, "Mercury", "closest to the sun", 0),
    Planet(2, "Venus", "very high temps", 0),
    Planet(3, "Earth", "home", 1),
    Planet(4, "Mars", "the red planet", 2),
    Planet(5, "Jupiter", "famous spot", 80),
    Planet(6, "Saturn", "famous rings", 83),
    Planet(7, "Uranus", "spins upside down", 27),
    Planet(8, "Neptune", "furthest from the sun", 14),
]

planet_bp = Blueprint("planets", __name__, url_prefix="/planets")


@planet_bp.route("", methods=["GET"])
def get_all_planets():
    planets_response = []
    for planet in PLANETS:
        planets_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "moon": planet.moon,
            }
        )

    return jsonify(planets_response)


@planet_bp.route("/<planet_id>", methods=["GET"])
def get_planet(planet_id):
    planet = validate_planet(planet_id)
    
    return {
        "id" : planet.id,
        "name" : planet.name,
        "description" : planet.description,
        "moon" : planet.moon
    }

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

    for planet in planets:
        if planet.id == planet_id:
            return planet

    abort(make_response({"message":f"planet {planet_id} not found"}, 404))
