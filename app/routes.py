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
    name_query = request.args.get("name")
    description_query = request.args.get("description")
    color_query = request.args.get("color")
    limit_query = request.args.get("limit")

    planet_query = Planet.query

    if name_query:
        planet_query = planet_query.filter_by(name=name_query)
    
    if description_query:
        planet_query = planet_query.filter_by(description=description_query)
    
    if color_query:
        color_query = planet_query.filter_by(color=color_query)

    if limit_query:
        limit_query = planet_query.limit(limit_query)

    planets = planet_query.all()

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