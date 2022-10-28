from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

# class Planet:
#     def __init__(self, id, name, description, size):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.size = size
# planets = [
#     Planet(1, "Mars", "red", "small"),
#     Planet(2, "Venus", "poisonous", "smallish"),
#     Planet(3, "Saturn", "has rings", "large")
# ]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

# def validate(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"message": f"Invalid planet id: '{planet_id}'"}, 400))
#     planet = Planet.query.get(planet_id)
#     if planet:
#         return planet

#     abort(make_response({"message": f'planet id {planet_id} not found'}, 404))

@planets_bp.route("", methods=["GET"])
def read_all_planets():
    request.method == "GET"
    planets = Planet.query.all()
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "size": planet.size
        })

    return jsonify(planets_response)

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name=request_body["name"], 
        description=request_body["description"],
        size=request_body["size"]
    )
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} created", 201)
    