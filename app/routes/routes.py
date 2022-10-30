from app import db
from flask import Blueprint, jsonify, make_response, request
from app.models.planet import Planet

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def handle_planets():  
    request_body = request.get_json() #converts request body into json object
    new_planet = Planet(name=request_body["name"],
                    description=request_body["description"],
                    moons = request_body["moons"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("", methods=["GET"])
def read_all_planets():
    planets_response = []
    planets = Planet.query.all()
    for planet in planets:
        planets_response.append(
                {
                    "id": planet.id,
                    "name": planet.name,
                    "description": planet.description,
                    "moons": planet.moons,
                }
            )
    return jsonify (planets_response), 200

#"""""" #####learn to docstring
# #OLD CODE BELOW
# #created Planet class
# class Planet:
#     def __init__(self, id, name, description, moons):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.moons = moons


#     #method in class planet.to_planet
#     def to_planet_dict(self):
#         return dict(
#             id=self.id, 
#             name=self.name, 
#             description=self.description,
#             moons=self.moons
#     )
# #created planet instances
# planets= [
#     Planet(1, "fi", "red planet", 10),
#     Planet(2, "fie", "blue planet", 9),
#     Planet(3, "foo", "yellow planet", 8)

# bp = Blueprint("planets", __name__, url_prefix="/planets") 
# #call method .to planets, return jsonified result from dictionary
# @bp.route("", methods=["GET"])
# def handle_planets():
#     results_list = []
#     for planet in planets: 
#                 results_list.append(planet.to_planet_dict())
#     return jsonify(results_list)

# #validate input for request
# def validate_planet(planet_id):
#     #if string cannot cast to integer, return "bad request"
#     try:
#         planet_id= int(planet_id)
#     except:
#         abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

#     #if planet.id not found, return 404
#     for planet in planets: 
#         if planet.id == planet_id:
#             return planet

#     abort(make_response({"message":f"planet {planet_id} not found"}, 404))

# #create endpoint blueprint
# @bp.route("/<id>", methods=["GET"])
# def handle_planet(id):
#     planet = validate_planet(id)
#     return jsonify(planet.to_planet_dict())

#     """"""