from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

planet_bp = Blueprint("planets", __name__, url_prefix="/planets")

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"the planet {cls.__name__} {model_id} is invalid, please search by planet_id."}, 400))

    planet = cls.query.get(model_id)

    if not planet:
        abort(make_response({"message":f"the planet {cls.__name__} {model_id} doesn't exist."}, 404))
    return planet

@planet_bp.route("/<model_id>", methods = ["GET"])
def get_one_planet(model_id):
    planet = validate_model(Planet, model_id)
    # planet = cls.query.get(model_id)
    return planet.to_dict()

@planet_bp.route("", methods=["GET"])
def get_all_planets():
    name_query = request.args.get("name")
    if name_query:
        planets = Planet.query.filter_by(name=name_query)
    else:
        planets = Planet.query.all()

    planet_response = []
    for planet in planets:
        planet_response.append(planet.to_dict())
    return jsonify(planet_response)

@planet_bp.route("", methods=["POST"])
def create_new_planet():
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planet_bp.route("/<model_id>", methods = ["PUT"])
def update_planet(model_id):
    planet = validate_model(Planet, model_id)
    request_body = request.get_json()
    planet = Planet.from_dict(request_body) # NEED TO FIX THIS LINE
    
    planet.name = request_body["name"],
    planet.color = request_body["color"],
    planet.moons = request_body["moons"],
    planet.livability = request_body["livability"],
    planet.is_dwarf = request_body["is_dwarf"]

    db.session.commit()

    return make_response(f"Planet #{model_id} successfully updated.")

@planet_bp.route("/<model_id>", methods = ["DELETE"])
def delete_planet(model_id):
    planet = validate_model(Planet, model_id)
    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{model_id} successfully deleted.")
    