from flask import Blueprint, jsonify, abort, make_response

"""
Define a Planet class with the attributes id, name, and description, 
and one additional attribute
"""


class Planet:
    def __init__(self, id, name, description, moon):
        self.id = id
        self.name = name
        self.description = description
        self.moon = moon

    # [Planet(1, "name"),  ]


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
    result = []
    for planet in PLANETS:
        result.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "moon": planet.moon,
            }
        )

    return jsonify(result)


def validate_planet_name(planet_name):
    try:
        planet_name = str(planet_name)
    except:
        abort(make_response({"message": f"planet {planet_name} invalid"}, 400))

    for planet in PLANETS:
        if planet.name == planet_name.capitalize():
            return planet

    abort(make_response({"message": f"planet {planet_name} not found"}, 404))


@planet_bp.route("/<planet_name>", methods=["GET"])
def get_one_planet(planet_name):
    planet = validate_planet_name(planet_name)

    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "moon": planet.moon,
    }
