from flask import Blueprint, jsonify, abort, make_response


class Planet:
    def __init__(self, id, name, description, moons):
        self.id = id
        self.name = name
        self.description = description
        self.moons = moons

    def to_planet_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            moons=self.moons
    )


planets = [
    Planet(1, "Mercury", "closest to the sun", 0),
    Planet(2, "Venus", "second closest to the sun", 0),
    Planet(3, "Earth", "where we live", 1)
]

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

    for planet in planets:
        if planet.id == planet_id:
            return planet

    abort(make_response({"message":f"planet {planet_id} not found"}, 404))

bp = Blueprint("planets", __name__, url_prefix = "/planets")

@bp.route("", methods=["GET"])
def handle_planets():
    results_list = []

    for planet in planets:
        results_list.append(planet.to_planet_dict())
        
    return jsonify(results_list)

@bp.route("/<planet_id>", methods=["GET"])
def handle_one_planet(planet_id):
    planet = validate_planet(planet_id)
    
    return jsonify(planet.to_planet_dict())
