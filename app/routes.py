from os import abort
from unicodedata import name
from app.models.planet import Planet
from app import db
from flask import Blueprint, jsonify, make_response, abort, request

bp = Blueprint("planets", __name__, url_prefix="/planets")

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)

    except:
        abort(make_response({"message":f"planet{planet_id} invalid"}, 400)) 

    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message": f"planet{planet_id} not found"}, 404))

    return planet



@bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet( 
        name=request_body["name"],
        description=request_body["description"])
        # miles_from_sun=request_body["miles"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@bp.route("", methods=["GET"])
def read_all_planets():
    planets_response = []
    planets = Planet.query.all()
    for planet in planets:
        planets_response.append(
            {
                "id" : planet.id,
                "name" : planet.name,
                "description" : planet.description
            }
        )
    return jsonify(planets_response)

@bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = Planet.query.get(planet_id)

    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description
        # "miles from sun" : planet.miles_from_sun
    }




@bp.route("/<planet_id>", methods=["PUT"])
def update_book(planet_id):
    planet = validate_planet(planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]

    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully updated")

@bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully deleted")