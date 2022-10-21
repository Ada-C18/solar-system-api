from flask import Blueprint, jsonify


class Planet:
    def __init__(self, id, name, description, num_moons):
        self.id = id
        self.name = name
        self.description = description
        self.num_moons = num_moons


planets = [
    Planet(1, 'Mercury', {"distance_from_sun": "36.04 million mi"}, 0),
    Planet(2, 'Venus', {"distance_from_sun": "67.24 million mi"}, 0),
    Planet(3, 'Earth', {"distance_from_sun": "92.96 million mi"}, 1),
    Planet(4, 'Mars', {"distance_from_sun": "141.60 million mi"}, 2),
    Planet(5, 'Jupiter', {"distance_from_sun": "483.80 million mi"}, 80),
    Planet(6, 'Saturn', {"distance_from_sun": "890.8 million mi"}, 83),
    Planet(7, 'Uranus', {"distance_from_sun": "1.784 billion mi"}, 27),
    Planet(8, 'Neptune', {"distance_from_sun": "2.793 billion mi"}, 14),
    Planet(9, 'Pluto', {"distance_from_sun": "3.70 billion mi"}, 5),
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


@planets_bp.route("", methods=["GET"])
def get_all_planets():
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "number of moons": planet.num_moons
        })
    return jsonify(planets_response)
