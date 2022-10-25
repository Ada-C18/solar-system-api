from flask import Blueprint, jsonify, abort, make_response

class Planet:
    def __init__(self, id, name, description, size):
        self.id = id
        self.name = name
        self.description = description
        self.size = size
planets = [
    Planet(1, "Mars", "red", "small"),
    Planet(2, "Venus", "poisonous", "smallish"),
    Planet(3, "Saturn", "has rings", "large")
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

def validate(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"Invalid planet id: '{planet_id}'"}, 400))
    planet = Planet.query.get(planet_id)
    if planet:
        return planet

    abort(make_response({"message": f'planet id {planet_id} not found'}, 404))

@planets_bp.route("", methods=["GET"])
def handle_planets():
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "size": planet.size
        })

    return jsonify(planets_response)
