from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request


def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"{cls.__name__} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)

    if not model:
        abort(make_response({"message":f"{cls.__name__} {model_id} not found"}, 404))

    return model

bp = Blueprint("planets", __name__, url_prefix = "/planets")

@bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    return jsonify(planet.to_dict()), 200

@bp.route("", methods=["GET"])
def read_all_planets():
    planets = Planet.query.all()
    planet_response = [planet.to_dict() for planet in planets]
    return jsonify(planet_response)

@bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)

    db.session.add(new_planet)
    db.session.commit()
    return make_response(f"Planet {new_planet.name} successfully created", 201)

@bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    request_body = request.get_json()
    
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.moons = request_body["moons"]

    db.session.commit()
    return make_response(f"Planet #{planet.id} successfully updated", 200)

@bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    db.session.delete(planet)
    db.session.commit()
    return make_response(f"Planet #{planet.id} successfully deleted", 200)