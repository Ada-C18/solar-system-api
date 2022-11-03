from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

planet_bp = Blueprint("planets", __name__, url_prefix = "/planets")

# HELPER FUNCTIONS
def validate_planet_id(planet_id):
    planet = validate_planet_id(planet_id)
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet #{planet_id} is invalid, please search by planet_id."}, 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message":f"planet #{planet_id} doesn't exist."}, 404))
    return planet

# MAIN FUNCTIONS HANDLING REQUESTS
@planet_bp.route("", methods=["GET"])
def get_planets():
# planet = validate_planet_id(planet_id)
    name_query = request.args.get("name")

    if name_query is not None:
        planets = Planet.query.filter_by(name=name_query)
    else:
        planets = Planet.query.all()
    
    planet_response = []
    for planet in planets:
        planet_response.append({
            "id": planet.id,
            "name": planet.name,
            "color": planet.color,
            "livability": planet.livability,
            "moons": planet.moons,
            "is_dwarf": planet.is_dwarf
        })
    return jsonify(planet_response)

@planet_bp.route("", methods=["POST"])
def create_new_planet():
    planet = validate_planet_id(planet.id)

    request_body = request.get_json()

    new_planet = Planet(
        name = request_body["name"],
        color = request_body["color"],
        moons = request_body["moons"],
        livability = request_body["livability"],
        is_dwarf = request_body["is_dwarf"]
    )

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planet_bp.route("/<planet_id>", methods = ["GET"])
def get_one_planet(planet_id):
    planet = validate_planet_id(planet_id)

    return {
            "id": planet.id,
            "name": planet.name,
            "color": planet.color,
            "livability": planet.livability,
            "moons": planet.moons,
            "is_dwarf": planet.is_dwarf
            }


@planet_bp.route("/<planet_id>", methods = ["PUT"])
def update_planet(planet_id):
    planet = validate_planet_id(planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"],
    planet.color = request_body["color"],
    planet.moons = request_body["moons"],
    planet.livability = request_body["livability"]
    planet.is_dwarf = request_body["is_dwarf"]

    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully updated.")

@planet_bp.route("/<planet_id>", methods = ["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet_id(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully deleted.")
