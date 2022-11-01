from os import abort
from unicodedata import name
from app.models.planet import Planet
from app import db
from flask import Blueprint, jsonify, make_response, abort, request

bp = Blueprint("planets", __name__, url_prefix="/planets")


@bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(id=request_body["id"], 
        name=request_body["name"],
        description=request_body["description"])
        # miles_from_sun=request_body["miles"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@bp.route("", methods=["GET"])
def read_all_planets():
    planets = Planet.query.all()
    planets_response = [planet.to_dict() for planet in planets]
    return jsonify(planets_response)


# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)

#     except:
#         abort(make_response({"message":f"planet{planet_id} invalid"}, 400)) 
    
#     for planet in planets:
#         if planet.id == planet_id:
#             return planet

#     abort(make_response({"message": f"planet{planet_id} not found"}, 404))

# @bp.route("/<id>", methods=["GET"])
# def handle_planet(id):
#     planet = validate_planet(id)
#     return jsonify(planet.to_json())