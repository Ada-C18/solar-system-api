from flask import Blueprint, jsonify


class Planet:
    def __init__(self, id, name, description, distance):
        self.id = id
        self.name = name
        self.description = description
        self.distance = distance


planet_list = [
    Planet(1, "Mercury", "tiny and hot", 0.387),
    Planet(2, "Venus", "big and hot", 0.722),
    Planet(3, "Earth", "home", 1.0),
]

bp = Blueprint("planets", __name__, url_prefix="/planet")


@bp.route("", methods=["GET"])
def handle_planets():
    planets_list = []
    for planet in planet_list:
        planets_list.append(
            dict(
                id=planet.id,
                name=planet.name,
                description=planet.description,
                distance=planet.distance,
            )
        )
    return jsonify(planets_list)
