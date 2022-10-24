# tell flask you want to import data
from flask import Blueprint, jsonify, abort, make_response

class Planet:

    def __init__(self, id, name, description, color):
        self.id = id
        self.name = name
        self.description = description
        self.color = color

planet_1 = Planet(1, "Planet 1", "small and round", "blue")
planet_2 = Planet(2, "Planet 2", "big and bouncy", "red")
planet_3 = Planet(3, "Planet 3", "wispy", "green")

PLANET_LIST = [
    planet_1,
    planet_2,
    planet_3
]

planets_bp = Blueprint('planets_bp', __name__, url_prefix='/planets')

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

    for planet in PLANET_LIST:
        if planet.id == planet_id:
            return planet

    abort(make_response({"message":f"planet {planet_id} not found"}, 404)) 

@planets_bp.route("/<planet_id>", methods=["GET"])
def return_planet(planet_id):
    planet = validate_planet(planet_id)

    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "color": planet.color
    }



@planets_bp.route("", methods=["GET"])
def return_planets():
    planets_list = []
    for planet in PLANET_LIST:

        planets_list.append(
            {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "color": planet.color
            }
        )
    return jsonify(planets_list)
