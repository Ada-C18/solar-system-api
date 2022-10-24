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
    Planet(5, "Jupiter",  "Biggest planet in the solar system", 80)
    Planet(6, "Saturn", "The planet with the rings", 83)
    Planet(7, "Uranus", "Ice giant", 27)
    Planet(8, "Neptune", "A cold blue planet", 14)
    Planet(9, "Pluto", "The tiniest dwarf planet", 5)
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