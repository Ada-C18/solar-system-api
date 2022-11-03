from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet

# planets = [
#     Planet(1, "Mercury", "solid", 0),
#     Planet(2, "Venus", "bright and volcanic", 0),
#     Planet(3, "Earth", "half and half", 1)
# ]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        moons=request_body["moons"])
    db.session.add(new_planet)
    db.session.commit()
    return make_response(f"Planet {new_planet.name} has been created successfully", 201)

@planets_bp.route("", methods=["GET"])
def read_all_planets():
    name_query = request.args.get("name")
    moons_query = request.args.get("moons")
    description_query = request.args.get("description")
    planet_query = Planet.query
    if name_query:
        planet_query = Planet.query.filter_by(name=name_query)
    if moons_query:
        planet_query = Planet.query.filter_by(moons=moons_query)
    if description_query:
        planet_query = Planet.query.filter_by(description=description_query)

    

    planets = planet_query.all()
    planets_response = [planet.to_dict() for planet in planets]

    return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def planet_endpoint(planet_id):
    planet = validate_planet(planet_id)

    return jsonify(planet.to_dict())

@planets_bp.route("/<planet_id>", methods=["PUT"])
def planet_update(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.moons = request_body["moons"]

    db.session.commit()
    return make_response(f"Planet {planet.name} has been updated successfully", 200)

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def planet_delete(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet {planet.name} has been deleted successfully", 200)

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))
    
    planet = Planet.query.get(planet_id)
    
    if not planet:
        abort(make_response({"message":f"planet {planet_id} not found"}, 404))

    return planet