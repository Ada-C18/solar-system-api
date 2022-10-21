from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, size):
        self.id = id
        self.name = name
        self.description = description
        self.size = size


planets = [
    Planet(1, "Saturn", "cold", "large"),
    Planet(2, "Earth", "normal", "medium"),
    Planet(3, "Jupiter", "sunny", "large")
        ]

bp = Blueprint("planets", __name__, url_prefix="/planets")

@bp.route("", methods=["GET"])
def all_planets():
    results_list = [dict(
            id=planet.id,
            name=planet.name,
            description=planet.description,
            size=planet.size
        ) for planet in planets]

    return jsonify(results_list)
    


