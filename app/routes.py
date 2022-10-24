from flask import Blueprint, jsonify

class Planet():
    def __init__(self, id, name, description, moon_count):
        self.id = id
        self.name = name
        self.description = description
        self.moon_count = moon_count

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