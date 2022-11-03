from app import db
from flask import Blueprint, jsonify, abort, make_response, request
from .models.planet import Planet

bp = Blueprint("planets", __name__, url_prefix="/planets")


def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"planet {planet_id} invalid"}, 400))

    planet = Planet.query.get(planet_id)
    if not planet:
        abort(make_response({"message": f"planet {planet_id} not found"}, 404))

    return planet

def validate_planet_dict(request_body):
    request_body = dict(request_body)
    if not request_body.get("name", False) or not request_body.get("description", False) or not request_body.get("rings", False):
        abort(make_response({'message': 'request body invalid; cannot create planet'}, 400))

@bp.route("", methods=["GET"])
def handle_planets():
    planets = Planet.query.all()
    planets_response = []
    for planet in planets:
        planets_response.append(planet.to_dict())
    return jsonify(planets_response)

@bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    validate_planet_dict(request_body)
    new_planet = Planet.from_dict(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)


@bp.route("/<planet_id>", methods=["GET"])
def handle_one_planet(planet_id):
    planet = validate_planet(planet_id)

    return jsonify(planet.to_dict())

@bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()
    validate_planet_dict(request_body)
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.rings = request_body["rings"]

    db.session.commit()
    return make_response(f"Planet #{planet.id} sucessfully updated"), 200

@bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)
    db.session.delete(planet)
    db.session.commit()
    return make_response(f"Planet #{planet.id} successfully deleted"), 200