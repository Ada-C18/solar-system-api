from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, flag):
        self.id = id
        self.name = name
        self.description = description
        self.flag = flag

planets = [ 
Planet(0, "jupiter", "largest planet in solar system", False),
Planet(1, "mercury", "smallest planet in solar system", False), 
Planet(2, "mars", "most explored planet in solar system", True)
]

planet_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planet_bp.route("", methods=["GET"])
def list_planets():
    planet_list = []
    for planet in planets:
        planet_list.append(dict(
        id = planet.id,
        name = planet.name,
        description = planet.description,
        flag = planet.flag
        ))
    return jsonify(planet_list)