from flask import Blueprint, jsonify, make_response, request, abort, make_response
from app.models.planet import Planet
from app import db

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"{cls.__name__} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)

    if not model:
        abort(make_response({"message":f"{cls.__name__} {model_id} not found"}, 404))
    
    return model

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body=request.get_json()
    new_planet = Planet.from_dict(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("", methods=["GET"])
def read_all_planets():
    planets = Planet.query.all()
    planets_response = [planet.to_dict() for planet in planets]

    return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def read_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "color": planet.color
    }

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.color = request_body["color"]

    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully updated")

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully deleted")