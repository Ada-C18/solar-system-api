from flask import Blueprint, jsonify, abort, make_response

class Planet:
    def __init__(self, id, name, description, size):
        self.id = id
        self.name = name
        self.description = description
        self.size = size

    def to_json(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            size=self.size
    )

planets = [
    Planet(1, "Saturn", "cold", "large"),
    Planet(2, "Earth", "normal", "medium"),
    Planet(3, "Jupiter", "sunny", "large")
        ]

bp = Blueprint("planets", __name__, url_prefix="/planets")

@bp.route("", methods=["GET"])
def all_planets():
    results_list = [planet.to_json() for planet in planets]

    return jsonify(results_list)

def  validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"planet {planet_id} invalid"}, 400))

    for planet in planets:
        if planet.id == planet_id:
            return planet
    abort(make_response({"message": f"planet {planet_id} not found"}, 404))


@bp.route("/<id>", methods = ["GET"])
def handle_planet (id):
    planet = validate_planet(id)
    return jsonify(planet.to_json())





