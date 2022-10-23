from flask import Blueprint, jsonify

class Planet():
    def __init__(self, id, name, description, color):
        self.id = id
        self.name = name
        self.description = description
        self.color = color

PLANETS = [
    Planet(1, "Saturn", "gassy giant", "orange"),
    Planet(2, "Mercury", "small rocky", "gray"),
    Planet(3, "Pluto", "still a planet", "white")
]

planet_bp = Blueprint("Planet", __name__, url_prefix="/planet")

@planet_bp.route("", methods=["GET"])
def handle_books():
    planets_response = []
    for planet in PLANETS:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "color": planet.color
        })
    return jsonify(planets_response)





