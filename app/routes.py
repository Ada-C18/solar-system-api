from flask import Blueprint, jsonify, abort, make_response

class Planet:
    def __init__(self, id, name, description, revolution_period):
       self.id = id
       self.name = name 
       self.description = description
       self.revolution_period = revolution_period

PLANETS = [
    Planet(1, "Mercury", "terrestrial", "87.97 days"),
    Planet(2, "Venus", "terrestrial", "224.7 days"),
    Planet(3, "Earth", "terrestrial", "365.26 days"),
    Planet(4, "Mars", "terrestrial", "1.88 years"),
    Planet(5, "Jupiter", "gaseous", "11.86 years"),
    Planet(6, "Saturn", "gaseous", "29.46 years"),
    Planet(7, "Uranus", "gaseous", "84.01 years"),
    Planet(8, "Neptune", "gaseous", "164.79 years"),
    Planet(9, "Pluto", "icy, rocky", "248.59 years")
]


planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

# @planets_bp.route("", methods=["GET"])
# def get_all_planets():
#     planet_response = []
#     for planet in PLANETS:
#         planet_response.append({
#             "id" : planet.id,
#             "name" : planet.name,
#             "description" : planet.description,
#             "revolution_period" : planet.revolution_period 
#         })

#     return jsonify(planet_response)

# ------------------ Refactoring get_all_planets with vars and list comprehension --------------------
@planets_bp.route("", methods=["GET"])
    
def get_all_planets():
    planet_response = [vars(planet) for planet in PLANETS]
    return jsonify(planet_response)

#GET one planet

def validate_planet(id):
    try:
        planet_id = int(id)
    except ValueError:
        return {
            'message': 'Invalid planet id'
        },400
    for planet in PLANETS:
        if planet.id == planet_id:
            return vars(planet)
    abort(make_response(jsonify(description = 'Planet not found'),404))
    # print(type(planet_response))
    # print(type(jsonify(planet_response)))

@planets_bp.route('/<id>',methods=['GET'])
def get_one_planet(id):
    planet = validate_planet(id)
    return planet
