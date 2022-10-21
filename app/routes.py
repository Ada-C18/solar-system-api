from flask import Blueprint, jsonify


class Planet:
    def __init__(self, id, name, description, radius):
        self.id = id
        self.name = name
        self.description = description
        self.radius = radius


planets = [
    Planet(1, 'Earth', 'good place', 6371 ), 
    Planet(2, 'Jupiter', 'fun place', 69901),
    Planet(3, 'Mars', 'weird place', 3389.5)
]

bp = Blueprint('planets', __name__, url_prefix='/planets')
@bp.route('', methods=["GET"])
def get_planets():
    planet_data = []
    for planet in planets:
        planet_data.append(dict(id=planet.id, name=planet.name, description=planet.description, radius=planet.radius))
    return jsonify(planet_data)
