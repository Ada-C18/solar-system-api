from flask import Blueprint, jsonify, abort, make_response

# class Planet:
#     def __init__(self, id, name, description, color):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.color = color

#     def to_planet_dict(self):
#         return dict(
#             id = self.id,
#             name = self.name,
#             description = self.description,
#             color = self.color
#         )

# planets = [
#     Planet(1, "Pluto", "Small", "Blue"),
#     Planet(2, "Mercury", "Hot, probably", "Red"),
#     Planet(3, "Mars", "Medium", "Orange")
# ]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])

def handle_planets():
    result = []
    for planet in planets:
        result.append(planet.to_planet_dict())
    return jsonify(result)

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"Planet {planet_id} invalid"}, 400))

    for planet in planets:
        if planet.id == planet_id:
            return planet

    abort(make_response({"message": f"Planet {planet_id} not found"}, 404))

@planets_bp.route("/<planet_id>", methods=["GET"])

def handle_planet(planet_id):
    planet = validate_planet(planet_id)
    return jsonify(planet.to_planet_dict())