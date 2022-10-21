from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, moons):
        self.id = id
        self.name = name
        self.description = description
        self.moons = moons

planets = [
    Planet(1, "Mercury", "closest to the sun", 0),
    Planet(2, "Venus", "second closest to the sun", 0),
    Planet(3, "Earth", "where we live", 1)
]

bp = Blueprint("planets", __name__, url_prefix = "/planets")

@bp.route("", methods=["GET"])

def handle_planets():
    results_list = []
    for planet in planets:
        results_list.append(dict(
            id=planet.id,
            name=planet.name,
            description=planet.description,
            moons=planet.moons

        ))

    return jsonify(results_list)