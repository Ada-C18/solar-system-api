from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request, abort

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} has been created", 201)


@planets_bp.route("", methods=["GET"])
def get_all_cats():
    name_param = request.args.get("name")
    diameter_param = request.args.get("diameter")

    if name_param:
        planets = Planet.query.filter_by(name=name_param)
    elif diameter_param:
        planets = Planet.query.filter_by(diameter=diameter_param)
    else:
        planets = Planet.query.all()

    result_list = [planet.to_dict() for planet in planets]

    return jsonify(result_list), 200


@planets_bp.route("/<id>", methods=["GET"])
def get_one_cat(id):
    planet = validate_id(Planet,id)

    return jsonify(planet.to_dict()), 200


@planets_bp.route("/<id>", methods=["PUT"])
def update_planet(id):
    planet = validate_id(Planet,id)
    request_body = request.get_json()

    planet.update(request_body)

    db.session.commit()

    return make_response(f"planet {id} successfully updated")

@planets_bp.route("/<id>", methods=["DELETE"])
def delete_planet(id):
    planet = validate_id(Planet,id)

    db.session.delete(planet)

    db.session.commit()

    return make_response(f"planet {id} successfully deleted")


def validate_id(class_obj,id):
    try:
        id = int(id)
    except:
        abort(make_response({"message":f"{class_obj} {id} is an invalid id"}, 400))

    query_result = class_obj.query.get(id)
    if not query_result:
        abort(make_response({"message":f"{class_obj} {id} not found"}, 404))

    return query_result


######## before wave 5 ################

# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

#     planet = Planet.query.get(planet_id)

#     if not planet:
#         abort(make_response({"message":f"planet {planet_id} not found"}, 404))

#     return planet

# @planets_bp.route("", methods=["POST"])
# def create_planet():
#     request_body = request.get_json()
#     new_planet = Planet(id=request_body["id"],
#                     name=request_body["name"],
#                     description=request_body["description"],
#                     diameter=request_body["diameter"])

#     db.session.add(new_planet)
#     db.session.commit()

#     return make_response(f"Planet {new_planet.id} successfully created", 201)

# @planets_bp.route("", methods=["GET"])
# def read_all_planets():
#     name_query = request.args.get("name")
#     if name_query:
#         planets = Planet.query.filter_by(name=name_query)
#     else:
#         planets = Planet.query.all()
    
#     planets_response = []
#     for planet in planets:
#         planets_response.append(
#             {
#                 "id": planet.id,
#                 "name": planet.name,
#                 "description": planet.description,
#                 "diameter": planet.diameter
#             }
#         )
#     return jsonify(planets_response)




# @planets_bp.route("/<planet_id>", methods=["GET"])
# def read_one_planet(planet_id):
#     planet = validate_planet(planet_id)
#     return {
#             "id":planet.id,
#             "name":planet.name,  
#             "description":planet.description,
#             "diameter":planet.diameter
#         }
    
# @planets_bp.route("/<planet_id>", methods=["PUT"])
# def update_planet(planet_id):
#     planet = validate_planet(planet_id)

#     request_body = request.get_json()

#     planet.name = request_body["name"]
#     planet.description = request_body["description"]
#     planet.diameter = request_body["diameter"]
    
#     db.session.commit()

#     return make_response(f"Planet # {planet.id} successfully updated")


# @planets_bp.route("/<planet_id>", methods=["DELETE"])
# def delete_planet(planet_id):
#     planet = validate_planet(planet_id)
    
#     db.session.delete(planet)
#     db.session.commit()
    
#     return make_response(f"Planet # {planet.id} successfully deleted")
    

    
# solar_system_bp = Blueprint("solar_system", __name__)


# class Planet:
#     def __init__(self, id, name, description, diameter):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.diameter = diameter
# planets = [
#     Planet(1, "Mercury", "The smallest planet in the solar system", 3031.9),
#     Planet(2, "Venus", "The hottest planet in the solar system", 7520.8),
#     Planet(3, "Earth", "Two-thirds of the planet is covered by water", 7917.5),
#     Planet(4, "Mars", "A dusty, cold, desert world", 4212.3),
#     Planet(5, "Jupiter", "The planet with swirling cloud stripes", 86881),
#     Planet(6, "Saturn", "A massive ball made mostly of hydrogen and helium", 72367),
#     Planet(7, "Uranus", "The first planet found, discovered in 1781", 31518),
#     Planet(8, "Neptune", "The densest giant planet", 30599),
    
# # ]
# planets_bp = Blueprint("planets_bp", __name__,  url_prefix="/planets") 

# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

#     for planet in planets:
#         if planet.id == planet_id:
#             return planet
    
#     abort(make_response({"message":f"planet {planet_id} not found"}, 404))

# @planets_bp.route("",methods=["GET"])  
# def handle_planets():
#     planets_response = []
#     for planet in planets:
#         planets_response.append(
#             {
#                 "id":planet.id,
#                 "name":planet.name,  
#                 "description":planet.description,
#                 "diameter":planet.diameter
#             }
#         )  
#     return jsonify(planets_response) 

    
# @planets_bp.route("/<planet_id>", methods=["GET"])
# def handle_planet(planet_id):
#     planet = validate_planet(planet_id)

#     return {
#         "id": planet.id,
#         "name": planet.name,  
#         "description": planet.description,
#         "diameter": planet.diameter
#     }