from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, color, description):
        self.id = id
        self.name = name
        self.color = color
        self.description = description

planets = [
    Planet(1, "Saturn", "yellowish-brown", "Saturn is the sixth planet from the Sun and the second-largest planet in our solar system."),
    Planet(2, "Mars", "rusty red", "Mars is the fourth planet from the Sun – a dusty, cold, desert world with a very thin atmosphere."),
    Planet(3, "Jupiter", "beige", "Jupiter is covered in swirling cloud stripes. It has big storms like the Great Red Spot, which has been going for hundreds of years. ")
]

planets_bp = Blueprint("planets_bp", __name__, url_prefix = "/planets")

@planets_bp.route("", methods = ["GET"])
def get_all_planets():
    planets_response = []
    for planet in planets:
        planets_response.append(
           {"id": planet.id,
            "name": planet.name,
            "color": planet.color,
            "description": planet.description
           }
        )
    return jsonify(planets_response)