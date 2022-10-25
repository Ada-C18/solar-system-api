
from flask import Blueprint , jsonify, abort, make_response

solar_system_bp = Blueprint("solar_system", __name__)

class Planet:
    def __init__(self, id, name, description, diameter):
        self.id = id
        self.name = name
        self.description = description
        self.diameter = diameter
planets = [
    Planet(1, "Mercury", "The smallest planet in the solar system", 3031.9),
    Planet(2, "Venus", "The hottest planet in the solar system", 7520.8),
    Planet(3, "Earth", "Two-thirds of the planet is covered by water", 7917.5),
    Planet(4, "Mars", "A dusty, cold, desert world", 4212.3),
    Planet(5, "Jupiter", "The planet with swirling cloud stripes", 86881),
    Planet(6, "Saturn", "A massive ball made mostly of hydrogen and helium", 72367),
    Planet(7, "Uranus", "The first planet found, discovered in 1781", 31518),
    Planet(8, "Neptune", "The densest giant planet", 30599),
    
]
planets_bp = Blueprint("planets_bp", __name__,  url_prefix="/planets") 

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

    for planet in planets:
        if planet.id == planet_id:
            return planet
    
    abort(make_response({"message":f"planet {planet_id} not found"}, 404))

@planets_bp.route("",methods=["GET"])  
def handle_planets():
    planets_response = []
    for planet in planets:
        planets_response.append(
            {
                "id":planet.id,
                "name":planet.name,  
                "description":planet.description,
                "diameter":planet.diameter
            }
        )  
    return jsonify(planets_response) 

    
@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planet = validate_planet(planet_id)

    return {
        "id": planet.id,
        "name": planet.name,  
        "description": planet.description,
        "diameter": planet.diameter
    }