from app import db
from flask import Blueprint, jsonify, make_response, abort, request
from app.models.planet_model import Planet

planets_bp = Blueprint('planets_bp', __name__, url_prefix='/planets')

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name=request_body["name"],
        description=request_body["description"]
        )

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} has been added to the Planets database.", 201)

@planets_bp.route("", methods=["GET"])
def all_planets():
    planets_response = []
    planets = Planet.query.all()

    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description
        })

    return jsonify(planets_response)


@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planet = Planet.query.get(planet_id)

    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description
    }


# REFACTOR TO CHANGE ALL DATA BASED ON ID!
@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]

    db.session.commit()

#     return make_response(f"Planet {new_planet.name} has been updated in the Planets database.", 200)



## REFACTOR TO DELETE ENTRY BASED ON ID!
@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = Planet.query.get(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet {planet.name} has been deleted from the Planets database.", 200)


''' Create a helper functions for:
        - 404 non-existing planet
        - 400 invalid planet id data type 
    & integrate functions to HTTP requests in routes '''

# # Helper Functions
def validate_planet(planet_id):
    try:
       planet_id = int(planet_id)
    except:
       abort(make_response({"message":f"Planet {planet_id} invalid"}, 400))

    planet = Planet.query.get(planet_id)
    if not planet:
        abort(make_response({"message":f"Planet {planet_id} not found"}, 404))
    
    return planet