from flask import Blueprint, jsonify

class Planet():
    def __init__(self, id, name, description, rings):
        self.id = id
        self.name = name
        self.description = description
        self.rings = rings

earth = Planet(3, "Earth", "Blue planet", False)
saturn = Planet(6, "Saturn", "Yellow", True)

planets = [earth, saturn]

bp = Blueprint("planets", __name__, url_prefix="/planets")

@bp.route("", methods=["GET"])
def handle_planets():
    planet_list = []
    for planet in planets:
        planet_list.append(dict(
            id = planet.id,
            name = planet.name,
            description = planet.description,
            rings = planet.rings))
    return jsonify(planet_list)