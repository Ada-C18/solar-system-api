from flask import Blueprint, jsonify, abort, make_response

#create planet class
class Planets:
    def __init__(self, id, name, description, livability):
        self.id = id
        self.name = name
        self.description = description
        self.livability = livability

    # planet instances
planets = [
    Planets(3, "earth", "green terrestrial planet", 10.0),
    Planets(2, "venus", "orange terrestrial planet", 4.5),
    Planets(4, "mars", "red terrestrial planet", 7.9),
    Planets(5, "jupiter", "beige gas giant", 1.6),
    Planets(8, "neptune", "blue ice giant", 3.4),
    ]

planets_bp = Blueprint("planets", __name__, url_prefix = "/planets")
    
@planets_bp.route("", methods = ["GET"])
#get all planets, return as a lists with all attributes
def get_planets():
    planet_response = []
    for planet in planets:
        planet_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "livability": planet.livability
        })
    return jsonify(planet_response)

# @planets_bp.route("/name", methods = ["GET"])
#validate the planet request    
def varify_planet_exist(id):
    try:
        id = int(id)
    except:
        # return {"message": f"planet {name} invalid"}, 400
        abort(make_response({"message":f"planet {id} is invalid, please search by planet_id."}, 400))

    for planet in planets:
        if planet.id == id:
            return planet

    abort(make_response({"message":f"planet {id} doesn't exist."}, 404))

@planets_bp.route("/<id>", methods = ["GET"])
#get ONE planet, send return if there's an error
def get_single_planet_by_id(id):
    planet = varify_planet_exist(id)

    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "livability": planet.livability,
    }

# SEARCH BY NAME DRAFT
# @planets_bp.route("/<name>", methods = ["GET"])
# #get ONE planet by name
# def get_single_planet_by_name(name):
#     for planet in planets:
#         if planet.name == name:
#             return {
#                 "id": planet.id,
#                 "name": planet.name,
#                 "description": planet.description,
#                 "livability": planet.livability,
#                 }
#         else:
#             return {"message":f"planet {name} doesn't exist."}, 404