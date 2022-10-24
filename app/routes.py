from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, color):
        self.id = id
        self.name = name
        self.description = description
        self.color = color

PLANETS = [
            Planet(1, "Pluto", "no longer a planet", "light blue"),
            Planet(2, "Mercury", "smallest planet out of the 8", "dark gray"),
            Planet(3, "Mars", "closest resemblance to Earth", "red")
        ]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    planets_response = []
    for planet in PLANETS:
        planets_response.append({
                                "id": planet.id, 
                                "name": planet.name, 
                                "description": planet.description,
                                "color": planet.color
                            })

    return jsonify(planets_response)