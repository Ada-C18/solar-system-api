from flask import Blueprint, jsonify, make_response, request
from app.models.planet import Planet
from app import db

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




def create_planet():
    request_body=request.get_json()
    new_planet = Planet(name = request_body["name"],
                description = request_body["description"],
                color = request_body["color"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("", methods=["GET"])
def read_all_planets():
    planets = Planet.query.all()
    planets_response = [planet.dict() for planet in planets]

    return jsonify(planets_response)