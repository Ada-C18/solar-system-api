
from os import abort
from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

######################### NEW VALIDATE FUNCTION ############################
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
def handle_planets():  
    request_body = request.get_json() #converts request body into json object
    new_planet = Planet.from_json(Planet, request_body)
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("", methods=["GET"])
def read_all_planets():

    #this code replaces the previous query
    name_query = request.args.get("name")
    description_query = request.args.get("description")
    moons_query = request.args.get("moons")
    if name_query:
        planets = Planet.query.filter_by(name=name_query)
    elif description_query:
        planets = Planet.query.filter_by(description=description_query)
    elif moons_query:
        planets = Planet.query.filter_by(moons=moons_query)
    else:
        planets = Planet.query.all()
    
    planets_response = []
    for planet in planets:
        planets_response.append(planet.to_dict())
    return jsonify (planets_response), 200

# GET ONE RESOURCE
@planets_bp.route("/<id>", methods=["GET"])
def get_one_planet(id):
    planet = validate_model(Planet, id)

    return planet.to_dict()

# UPDATE RESOURCE
@planets_bp.route("/<id>", methods=["PUT"])
def update_planet(id):
    planet = validate_model(Planet, id)
    request_body = request.get_json()
    
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.moons = request_body["moons"]

    db.session.commit()

    return make_response(f"planet {id} successfully updated")

# DELETE RESOURCE
@planets_bp.route("/<id>", methods=["DELETE"])
def delete_planet(id):
    planet = validate_model(Planet, id)

    db.session.delete(planet)

    db.session.commit()

    return make_response(f"planet {id} successfully deleted")
