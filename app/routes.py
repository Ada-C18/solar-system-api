from flask import Blueprint, jsonify, make_response, abort

class Planet:
    def __init__(self, id, name, description):
        self.id = id 
        self.name = name
        self.description = description

PLANETS = [
    Planet(1, "Mercury","The smallest planet in our solar system and closest to the Sun."),
    Planet(2, "Venus","Venus spins slowly in the opposite direction from most planets."),
    Planet(3, "Earth","Our home planet—is the only place we know of so far that’s inhabited by living things."),
    Planet(4, "Mars","Mars is a dusty, cold, desert world with a very thin atmosphere."),
    Planet(5, "Jupiter", "The largest planet in the solar system."),
    Planet(6, "Saturn", "Adorned with thousands of beautiful ringlets made of chunks of ice and rock."),
    Planet(7, "Uranus", "Uranus is an ice giant."),
    Planet(8, "Neptune","Dark, cold, and whipped by supersonic winds.")
    ]
planets_bp = Blueprint('planets_bp', __name__, url_prefix='/planets')

@planets_bp.route('', methods=['GET'])
def get_all_planets():
    planets = []
    for planet in PLANETS:
        planets.append({
            "id": planet.id,
            "planet": planet.name,
            "description": planet.description
        })
    return jsonify(planets)

@planets_bp.route('/<planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet_id = int(planet_id)
    planets = []
    for planet in PLANETS:
        planets.append({
            "id": planet.id,
            "planet": planet.name,
            "description": planet.description
        })
    return jsonify(planets[planet_id - 1])

