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
def validate_planet(planet_id, planets):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"Planet {planet_id} invalid"}, 400))

    for planet in planets:
        if planet.id == planet_id:
            return planet

    abort(make_response({"message": f"Planet {planet_id} not found"}, 404))

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
    planets = Planet.query.all()
    planet = validate_planet(planet_id, planets)
    
    return planet_dict(planet)