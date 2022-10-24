from unicodedata import name
from flask import Blueprint, jsonify

class Planet:

    def __init__(self, id, name, description, moons):
        self.id = id
        self.name = name
        self.description = description
        self.moons = moons

planets = [
    Planet(1, "Earth", "our home", 1),
    Planet(2, "Mars", "red planet", 2),
    Planet(3, "Pluto", "is a planet", 5)
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def handle_planets():
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "moons": planet.moons
    })
    return jsonify(planets_response)