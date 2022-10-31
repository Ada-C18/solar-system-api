from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

planet_bp = Blueprint("planets", __name__, url_prefix = "/planets")

@planet_bp.route("", methods=["POST", "GET"])
def handle_planets():
    request_body = request.get_json()
    if request.method == "GET":
        planets = Planet.query.all()
        planet_response = []
        for planet in planets:
            planet_response.append({
                "id": planet.id,
                "name": planet.name,
                "color": planet.color,
                "livability": planet.livability,
                "moons": planet.moons
            })
        return jsonify(planet_response)
    
    elif request.method == "POST": 
        new_planet = Planet(
        # id = request_body["id"],
        name = request_body["name"],
        color = request_body["color"],
        moons = request_body["moons"],
        livability = request_body["livability"]
        # is_dwarf = request_body["is_dwarf"]
        )

        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"Planet {new_planet.name} successfully created", 201)


# GET ONE PLANET BASED ON ID
def validate_planet_id(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        # return {"message": f"planet {name} invalid"}, 400
        abort(make_response({"message":f"planet #{planet_id} is invalid, please search by planet_id."}, 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message":f"planet #{planet_id} doesn't exist."}, 404))

    return planet

@planet_bp.route("/<planet_id>", methods = ["GET"])
def get_one_planet(planet_id):
    planet = validate_planet_id(planet_id)

    return {
            "id": planet.id,
            "name": planet.name,
            "color": planet.color,
            "livability": planet.livability,
            "moons": planet.moons
            }

@planet_bp.route("/<planet_id>", methods = ["PUT"])
def update_planet(planet_id):
    planet = validate_planet_id(planet_id)

    request_body = request.get_json()

    # planet.name = request_body["name"],
    # planet.color = request_body["color"],
    # planet.moons = request_body["moons"],
    planet.livability = request_body["livability"]

    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully updated.")

@planet_bp.route("/<planet_id>", methods = ["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet_id(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully deleted.")

#create planet class
# class Planets:
#     def __init__(self, id, name, description, livability):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.livability = livability

    # planet instances
# planets = [
#     Planets(3, "earth", "green terrestrial planet", 10.0),
#     Planets(2, "venus", "orange terrestrial planet", 4.5),
#     Planets(4, "mars", "red terrestrial planet", 7.9),
#     Planets(5, "jupiter", "beige gas giant", 1.6),
#     Planets(8, "neptune", "blue ice giant", 3.4),
#     ]
    
# @planets_bp.route("", methods = ["GET"])
#get all planets, return as a lists with all attributes
# def get_planets():
#     planet_response = []
#     for planet in planets:
#         planet_response.append({
#             "id": planet.id,
#             "name": planet.name,
#             "description": planet.description,
#             "livability": planet.livability
#         })
#     return jsonify(planet_response)

# @planet_bp.route("/<id>", methods = ["GET"])
#get ONE planet, send return if there's an error
# def get_single_planet_by_id(name):
#     planet = varify_planet_exist(name)

#     return {
#         "id": planet.id,
#         "name": planet.name,
#         "color": planet.color,
#         # "description": planet.description,
#         "livability": planet.livability,
#         "moons": planet.moons
#     }

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