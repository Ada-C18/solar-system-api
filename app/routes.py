from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request
from app.routes_helper_functions import validate_model

bp = Blueprint("planets", __name__, url_prefix = "/planets")

@bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    return jsonify(planet.to_dict()), 200

@bp.route("", methods=["GET"])
def read_all_planets():
    name_query = request.args.get("name")
    description_query = request.args.get("description")
    moons_query = request.args.get("moons")
    limit_query = request.args.get("limit")

    planet_query = Planet.query

    if name_query:
        planet_query = planet_query.filter_by(name=name_query)

    if description_query:
        planet_query = planet_query.filter_by(description=description_query)

    if moons_query:
        planet_query = planet_query.filter_by(moons=moons_query)

    if limit_query:
        planet_query = planet_query.limit(limit_query)

    planets = planet_query.all()

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