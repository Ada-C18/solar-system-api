from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet


# class Planet():
#     def __init__(self, id, name, description, moons):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.moons = moons

# list_of_planets = [
#     Planet(1, "Mercury", "Grey smallest planet",0),
#     Planet(2, "Venus", "Orange planet of love", 0),
#     Planet(3, "Earth", "Our planet!", 1),
#     Planet(4, "Mars", "Red planet that we're exploring", 2),
#     Planet(5, "Jupiter",  "Biggest planet in the solar system", 80),
#     Planet(6, "Saturn", "The planet with the rings", 83),
#     Planet(7, "Uranus", "Ice giant", 27),
#     Planet(8, "Neptune", "A cold blue planet", 14),
#     Planet(9, "Pluto", "The tiniest dwarf planet", 5),
# ]

# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

#     for planet in list_of_planets:
#         if planet.id == planet_id:
#             return planet

#     abort(make_response({"message":f"planet {planet_id} not found"}, 404))

#for handling errors:

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message":f"planet {planet_id} not found"}, 404))

    return planet


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def create_new_planet():
    request_body = request.get_json(force=True)
    new_planet = Planet(name=request_body["name"],
                    description=request_body["description"], moons=request_body["moons"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("", methods=["GET"])
def read_all_planets():

    name_query = request.args.get("name")
    if name_query:
        planets = Planet.query.filter_by(name=name_query)
    else:
        planets = Planet.query.all()
    planets_response = []
    
    for planet in planets:
        planets_response.append(planet.to_dict())
    return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return planet.to_dict()


# @planets_bp.route("", methods=["GET"])
# def show_all_planets():
#     planets_response = []
#     for planet in list_of_planets:
#         planets_response.append({
#             "id": planet.id,
#             "name": planet.name,
#             "description": planet.description,
#             "number of moons": planet.moons 
#         })
#     return jsonify(planets_response)

# @planets_bp.route("/<planet_id>", methods=["GET"])
# def get_planet_info(planet_id):
#     planet = validate_planet(planet_id)
#     return {
#         "id": planet.id,
#         "name": planet.name,
#         "description": planet.description,
#         "number of moons": planet.moons
#     }

