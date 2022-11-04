from app import db
from models.planet import Planet 
from flask import Blueprint, jsonify, abort, request, make_response

# HELPER FUNCTIONS #

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"{cls.__name__} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)

    if not model:
        abort(make_response({"message":f"{cls.__name__} {model_id} not found"}, 404))

    return model

# ROUTE FUNCTIONS # 

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    if "name" not in request_body or "description" not in request_body or "moon_count" not in request_body:
        return make_response("Invalid Request", 400)

        
    new_planet = Planet.from_dict(request_body)
    db.session.add(new_planet)
    db.session.commit()
    return make_response(jsonify(f"Planet {new_planet.name} successfully created"), 201)

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    name_query = request.args.get("name")
    moon_count_query = request.args.get("moon_count")

    if name_query:
        all_planets = Planet.query.filter_by(name=name_query)
    elif moon_count_query:
        all_planets = Planet.query.filter_by(moon_count=moon_count_query)
    else:
        all_planets = Planet.query.all()

    return jsonify([planet.to_dict() for planet in all_planets]), 200

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    request_body = request.get_json()

    planet = planet.update(request_body)

    db.session.commit()
    return make_response(jsonify(f"Planet {planet} successfully updated"))

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    return planet.to_dict()

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    
    db.session.delete(planet)
    db.session.commit()

    return make_response(jsonify(f"Planet #{planet.id} successfully deleted"))
