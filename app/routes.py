from flask import Blueprint, jsonify

class Planet():
    def __init__(self, id, name, description, moons):
        self.id = id
        self.name = name
        self.description = description
        self.moons = moons

list_of_planets = [
    Planet(1, "Mercury", "Grey smallest planet",0),
    Planet(2, "Venus", "Orange planet of love", 0),
    Planet(3, "Earth", "Our planet!", 1),
    Planet(4, "Mars", "Red planet that we're exploring", 2)
]

planets_bp = Blueprint("planets", __name__)

@planets_bp.route("/planets", methods=["GET"])
def show_all_planets():
    planets_response = []
    for planet in list_of_planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "number of moons": planet.moons 
        })
    return jsonify(planets_response)