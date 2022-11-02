# tell flask you want to import data
from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request, abort

# create blueprint so the endpoint /planets can access planets data
planets_bp = Blueprint('planets_bp', __name__, url_prefix='/planets')


def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)

    except:
        abort(make_response({"message": f"planet {planet_id} invalid"}, 400))

    planet = Planet.query.get(planet_id)
    if not planet:
        abort(make_response({"message": f"planet {planet_id} not found"}, 404))
    return planet


@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name=request_body["name"],
        description=request_body["description"],
        color=request_body["color"])

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
                "color": planet.color
            }
        )
    return jsonify(planets_response)


# allow user to replace a planet
@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.color = request_body["color"]

    db.session.commit()

    return make_response(f"Planet {planet.name} successfully updated", 201)


# allow user to choose which aspects of a planet to update
@planets_bp.route("/<planet_id>", methods=["PATCH"])
def patch_planet(planet_id):
    planet = validate_planet(planet_id)

    request_body = request.get_json()

    try:
        planet.name = request_body["name"]
    except: 
        pass

    try: 
        planet.description = request_body["description"]
    except: 
        pass

    try:
        planet.color = request_body["color"]
    except:
        pass


    db.session.commit()
    return make_response(f"Planet {planet.name} successfully updated", 201)


@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet {planet.name} successfully deleted", 200)


# allow get method for /planets/id
@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(planet_id)

    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "color": planet.color
    }
