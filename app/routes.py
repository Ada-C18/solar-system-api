from flask import Blueprint, jsonify

class Planet():
    def __init__(self, id, name, description, rings):
        self.id = id
        self.name = name
        self.description = description
        self.rings = rings

    def to_json(self):
        return dict(
            id = self.id,
            name = self.name,
            description = self.description,
            rings = self.rings)


earth = Planet(3, "Earth", "Blue planet", False)
saturn = Planet(6, "Saturn", "Yellow", True)

planets = [earth, saturn]

bp = Blueprint("planets", __name__, url_prefix="/planets")

@bp.route("", methods=["GET"])
def handle_planets():
    planet_list = []
    for planet in planets:
        planet_list.append(planet.to_json())
    return jsonify(planet_list)

@bp.route("/<planet_id>", methods = ["GET"])
def handle_planet(planet_id):
    try:
        planet_id = int(planet_id)

    except:
        return {"message":f"planet {planet_id} invalid"}, 400

    for planet in planets:
        if planet.id == planet_id:
            return jsonify(planet.to_json())
        
    return {"message":f"planet {planet_id} not found"}, 404