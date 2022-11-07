from unicodedata import name
from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet

# class Planet:

#     def __init__(self, id, name, description, moons):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.moons = moons

# planets = [
#     Planet(1, "Earth", "our home", 1),
#     Planet(2, "Mars", "red planet", 2),
#     Planet(3, "Pluto", "is a planet", 5)
# ]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    if ("name" not in request_body or "description" not in request_body
    or "moons" not in request_body):
        return make_response(f"Invalid Request", 400)
    
    new_planet = Planet.from_dict(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return make_response(
        f"Planet {new_planet.name} successfully created", 201
    )

@planets_bp.route("", methods=["GET"])
def read_all_planets():
    planets_response = []
    planets = Planet.query.all()
    for planet in planets:
    #     planets_response.append({
    #         "id": planet.id,
    #         "name": planet.name,
    #         "description": planet.description,
    #         "moons": planet.moons
    # })
        planets_response.append(planet.to_dict())
    return jsonify(planets_response)

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"{cls.__name__} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)

    if not model:
        abort(make_response({"message":f"{cls.__name__} {model_id} not found"}, 404))

    return model

@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    return planet.to_dict()
    # return {
    #     "id": planet.id,
    #     "name": planet.name,
    #     "description": planet.description,
    #     "moons": planet.moons,
    # }

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    
    request_body = request.get_json()
    
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.moons = request_body["moons"]
    
    db.session.commit()
    
    return make_response(f"Planet #{planet.id} successfully updated")

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully deleted")