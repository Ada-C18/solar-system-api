from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

solar_system_bp = Blueprint(
    "solar_system_bp", __name__, url_prefix="/solar-system"
    )

def verify_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"{cls.__name__} {model_id} invalid"}, 400))
    
    model = cls.query.get(model_id)
    if not model:
        abort(make_response(
        {"message":f"{cls.__name__} {model_id} not found"}, 404
        ))
    
    return model

@solar_system_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)
()
@solar_system_bp.route("", methods=["GET"])
def read_all_planets():
    name_query = request.args.get("name")
    distance_from_sun_query = request.args.get("distance_from_sun")
    limit_query = request.args.get("limit")

    planet_query = Planet.query

    if name_query:
        planet_query = planet_query.filter_by(name=name_query)

    if distance_from_sun_query:
        planet_query = planet_query.filter_by(distance_from_sun=distance_from_sun_query)

    if limit_query:
        planet_query = planet_query.limit(limit_query)

    planets = planet_query.all()

    planets_response = [planet.make_a_dict() for planet in planets]

    return jsonify(planets_response)

@solar_system_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = verify_model(Planet, planet_id)
    return jsonify(planet.make_a_dict()), 200

@solar_system_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = verify_model(Planet, planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.distance_from_sun = request_body["distance_from_sun"]
    planet.description = request_body["description"]

    db.session.commit()
    return make_response(f"Planet #{planet.id} successfully updated"), 200

@solar_system_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = verify_model(Planet, planet_id)
    db.session.delete(planet)
    db.session.commit()
    return make_response(f"Planet #{planet.id} successfully deleted"), 200