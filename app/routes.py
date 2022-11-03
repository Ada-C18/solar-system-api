from flask import Blueprint, jsonify, abort, make_response, request
from .models.planet import Planet
from app import db

# class Planet:
#     def __init__(self, id, name, description, color):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.color = color

# # PLANETS = [
#             Planet(1, "Pluto", "no longer a planet", "light blue"),
#             Planet(2, "Mercury", "smallest planet out of the 8", "dark gray"),
#             Planet(3, "Mars", "closest resemblance to Earth", "red")
#         ]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

#---HELPER FUNCTIONS---
def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"Planet {planet_id} invalid"}, 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message": f"Planet {planet_id} not found"}, 404))

    return planet



#---ROUTES---
@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet.new_instance_from_dict(request_body)
    
    db.session.add(new_planet)
    db.session.commit()

    return make_response(jsonify(f"Planet {new_planet.name} successfully created."), 201)

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    name_query = request.args.get("name")
    description_query = request.args.get("description")
    color_query = request.args.get("color")

    if name_query:
        planets = Planet.query.filter_by(name=name_query)
    elif description_query:
        planets = Planet.query.filter_by(description=description_query)
    elif color_query:
        planets = Planet.query.filter_by(color=color_query)
    else:
        planets = Planet.query.all()
    
    planets_response = [planet.create_dict() for planet in planets]

    return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)
    
    return planet.create_dict()

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):

    planet = validate_planet(planet_id)
    
    request_body = request.get_json()

    planet.update(request_body)

    db.session.commit()

    return make_response(f"Planet {planet.id} successfully updated.", 200)

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet {planet.id} successfully deleted.", 200)