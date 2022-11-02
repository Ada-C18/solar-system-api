from app import db
from flask import Blueprint, jsonify, abort, make_response, request
from app.models.planet import Planet

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def handle_planets():  
    request_body = request.get_json() #converts request body into json object
    new_planet = Planet(name=request_body["name"],
                    description=request_body["description"],
                    moons = request_body["moons"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("", methods=["GET"])
def read_all_planets():
    planets_response = []
    planets = Planet.query.all()
    for planet in planets:
        planets_response.append(
                {
                    "id": planet.id,
                    "name": planet.name,
                    "description": planet.description,
                    "moons": planet.moons,
                }
            )
    return jsonify (planets_response), 200

# GET ONE RESOURCE
@planets_bp.route("/<id>", methods=["GET"])
def get_one_planet(id):
    planet = validate_planet(id)

    return jsonify({
    "id": planet.id, 
    "name": planet.name, 
    "description": planet.description,
    "moons": planet.moons
}), 200

# UPDATE RESOURCE
@planets_bp.route("/<id>", methods=["PUT"])
def update_planet(id):
    planet = validate_planet(id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.moons = request_body["moons"]

    db.session.commit()

    return make_response(f"planet {id} successfully updated")

# DELETE RESOURCE
@planets_bp.route("/<id>", methods=["DELETE"])
def delete_planet(id):
    planet = validate_planet(id)

    db.session.delete(planet)

    db.session.commit()

    return make_response(f"planet {id} successfully deleted")

#validate input for request
def validate_planet(planet_id):
    #if string cannot cast to integer, return "bad request"
    try:
        planet_id= int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

    #if planet.id not found, return 404
    planet = Planet.query.get(planet_id)
    if not planet:
        abort(make_response({"message":f"planet {planet_id} not found"}, 404))

    return planet
    
