from crypt import methods
from unicodedata import name
from flask import Blueprint, jsonify, abort, make_response

class Planet:
    def __init__(self, id, name, description,):
        self.id = id 
        self.name = name
        self.description = description

PLANETS = [
    Planet(1, "Mercury","the smallest planet in our solar system and closest to the Sun" ),
    Planet(2, "Venus","Venus spins slowly in the opposite direction from most planets. A thick atmosphere traps heat in a runaway greenhouse effect, making it the hottest planet in our solar system."),
    Planet(3, "Earth","our home planet—is the only place we know of so far that’s inhabited by living things. It's also the only planet in our solar system with liquid water on the surface." ),
    Planet(4, "Mars","our home planet—is the only place we know of so far that’s inhabited by living things. It's also the only planet in our solar system with liquid water on the surface." ),
    Planet(5, "Jupiter", "the largest planet in the solar system. Jupiter's stripes and swirls are actually cold, windy clouds of ammonia and water, floating in an atmosphere of hydrogen and helium."),
    Planet(6, "Saturn", "Adorned with thousands of beautiful ringlets made of chunks of ice and rock. Like fellow gas giant Jupiter, Saturn is a massive ball made mostly of hydrogen and helium"),
    Planet(7, "Uranus", "Uranus is an ice giant. Most of its mass is a hot, dense fluid of icy materials – water, methane and ammonia – above a small rocky core. Like Venus, Uranus rotates east to west. But Uranus is unique in that it rotates on its side"),
    Planet(8, "Neptune","Dark, cold, and whipped by supersonic winds, ice giant Neptune is the eighth and most distant planet in our solar system. Neptune is the only planet in our solar system not visible to the naked eye" ),
    Planet(9, "Pluto", "Pluto has a heart-shaped glacier that’s the size of Texas and Oklahoma. This fascinating world has blue skies, spinning moons, mountains as high as the Rockies, and it snows – but the snow is red"),
]
planets_bp = Blueprint('planets_bp', __name__, url_prefix='/planets')

@planets_bp.route('', methods=['GET'])
def get_all_planets():
    planets_response = [vars(planet) for planet in PLANETS]
    
    return jsonify(planets_response)

# Get one planet
@planets_bp.route('/<name>', methods=['GET'])
def get_one_planet(name):
    # return planet as dict
    planet = validate_planet(name)
    return planet



def validate_planet(name):

    try:
            planet_name = str(name)
    except ValueError:
            return {
                    "message": "Invalid planet name"
                }, 400


    for planet in PLANETS:
        if planet.name == planet_name:
            return vars(planet)
    
    
    abort(make_response(jsonify(description="Resource not found"),404)) 