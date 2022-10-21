from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, color):
        self.id = id
        self.name = name
        self.description = description
        self.color = color

planets = [
    Planet(1, "Pluto", "Small", "Blue"),
    Planet(2, "Mercury", "Hot, probably", "Red"),
    Planet(3, "Mars", "Medium", "Orange")
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])

def handle_planets():
    result = []
    for planet in planets:
        result.append(dict(
            id = planet.id,
            name = planet.name,
            description = planet.description,
            color = planet.color
        ))
    return jsonify(result)