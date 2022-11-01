# tell flask you want to import data
from app import db 
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request 

# create planet class
class Planet:

    def __init__(self, id, name, description, color):
        self.id = id
        self.name = name
        self.description = description
        self.color = color

# create a list of 3 instances of planet class
# should this also be a function?
# PLANET_1 = Planet(1, "Planet 1", "small and round", "blue")
# PLANET_2 = Planet(2, "Planet 2", "big and bouncy", "red")
# PLANET_3 = Planet(3, "Planet 3", "wispy", "green")

# PLANET_LIST = [
#     PLANET_1,
#     PLANET_2,
#     PLANET_3
# ]

# create blueprint so the endpoint /planets can access planets data
# do we need another blueprint for /planets/id?
planets_bp = Blueprint('planets_bp', __name__, url_prefix='/planets')

# validate planet
# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"message":f"planet {planet_id} invalid"}, 400))


#     # for planet in PLANET_LIST:
#     #     if planet.id == planet_id:
#     #         return planet

#     try:
#         this_planet = [planet for planet in PLANET_LIST if planet.id == planet_id]
#         return this_planet[0] 

#     except:
#         abort(make_response({"message":f"planet {planet_id} not found"}, 404)) 

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                    description=request_body["description"],
                    color=request_body["color"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

# allow get method for /planets/id (I think)
# @planets_bp.route("/<planet_id>", methods=["GET"])
# def read_one_planet(planet_id):
#     planet = validate_planet(planet_id)

#     return {
#         "id": planet.id,
#         "name": planet.name,
#         "description": planet.description,
#         "color": planet.color
#     }

# allow get method for /planets
# @planets_bp.route("", methods=["GET"])
# def read_planets():
#     planets_list = []
#     for planet in PLANET_LIST:

#         planets_list.append(
#             {
#             "id": planet.id,
#             "name": planet.name,
#             "description": planet.description,
#             "color": planet.color
#             }
#         )
        
#     return jsonify(planets_list)


