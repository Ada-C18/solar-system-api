from flask import Blueprint, jsonify, abort, make_response

class Planet:
    def __init__(self, id, name, description, moons):
        self.id = id
        self.name = name
        self.description = description
        self.moons = moons


planets = [
    Planet(1, "Mercury", "solid", 0),
    Planet(2, "Venus", "bright and volcanic", 0),
    Planet(3, "Earth", "half and half", 1)
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def planets_endpoint():
    response = []
    for planet in planets:
        response.append(
            dict(
                id = planet.id,
                name = planet.name,
                description = planet.description,
                moons = planet.moons
            )
        )
    return jsonify(response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def planet_endpoint(planet_id):
    planet = validate_planet(planet_id)
    return dict(
            id = planet.id,
            name = planet.name,
            description = planet.description,
            moons = planet.moons
        )

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

    for planet in planets:
        if planet.id == planet_id:
            return planet

    abort(make_response({"message":f"planet {planet_id} not found"}, 404))