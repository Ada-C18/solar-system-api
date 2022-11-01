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

@planet_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)
    # planet = Planet.query.get(planet_id)

    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "color": planet.color
    }

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message":f"planet {planet_id} not found"}, 404))

    return planet

@planet_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.color = request_body["color"]

    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully updated")

@planet_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"planet #{planet.id} successfully deleted")



