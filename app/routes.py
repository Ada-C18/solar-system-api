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

def planet_dict(planet):
    return {
        "id": planet.id, 
        "name": planet.name, 
        "description": planet.description,
        "color": planet.color
    }

#---ROUTES---
@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(
                        name = request_body["name"],
                        description = request_body["description"],
                        color = request_body["color"]
                        )
    
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created.", 201)

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    planets = Planet.query.all()
    planets_response = []

    for planet in planets:
        planets_response.append(planet_dict(planet))

    return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)
    
    return planet_dict(planet)

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.color = request_body["color"]

    db.session.commit()

    return make_response(f"Planet {planet.id} successfully updated.", 200)

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet {planet.id} successfully deleted.", 200)