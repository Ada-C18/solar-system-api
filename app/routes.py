from flask import Blueprint, jsonify, abort, make_response

class Planet():
    def __init__(self, id, name):#removed description and moon_count for now
        self.id = id
        self.name = name
        # self.description = description
        # self.moon_count = moon_count

PLANETS = [
    Planet(1, "Mercury"),
    Planet(2, "Venus"),
    Planet(3, "Mars"),
    Planet(4, "Earth"),
    Planet(5, "Jupiter"),
    Planet(6, "Saturn"),
    Planet(7, "Uranus"),
    Planet(8, "Neptune")
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    result = [vars(planet) for planet in PLANETS]
    return jsonify(result)

def validate_planet(planet_id): 
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"{planet_id} is invalid"}, 400))
    
    for planet in PLANETS:
        if planet.id == planet_id:
            return vars(planet)
    abort(make_response({"message": f"{planet_id} not found"}, 404))

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return planet
