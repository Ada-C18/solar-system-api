from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet

# class Planet():
#     def __init__(self, id, name, description, color):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.color = color

# PLANETS = [
#     Planet(1, "Saturn", "gassy giant", "orange"),
#     Planet(2, "Mercury", "small rocky", "gray"),
#     Planet(3, "Pluto", "still a planet", "white")
# ]

planet_bp = Blueprint("Planet", __name__, url_prefix="/planet")

@planet_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name=request_body['name'], 
        description=request_body['description'], 
        color=request_body['color']
    )
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} has been created", 201)

@planet_bp.route("", methods=["GET"])
def get_all_planets():
    results_list = []
    all_planets = Planet.query.all()

    for planet in all_planets:
        results_list.append({
        "name": planet.name,
        "color": planet.color,
        "description": planet.description,
        "id": planet.id
    })
    return jsonify(results_list),200





