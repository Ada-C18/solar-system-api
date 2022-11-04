from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


def validate_id(class_obj, id):
    try:
        id = int(id)
    except:
        abort(make_response({"message": f"{class_obj} {id} invalid"}, 400))

    query_result = Planet.query.get(id)

    if not query_result:
        abort(make_response({"message": f"{class_obj} {id} not found"}, 404))

    return query_result


@planets_bp.route("", methods=["POST"])
def add_planet():
    request_body = request.get_json()
    new_planet = Planet.create_from_json(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully added", 201)


@planets_bp.route("", methods=["GET"])
def read_all_planets():
    name_query = request.args.get("name")
    moon_query = request.args.get("moons")
    if name_query:
        planets = Planet.query.filter_by(name=name_query)
    if moon_query:
        planets = Planet.query.filter_by(moon=moon_query)
    else:
        planets = Planet.query.all()

    planets_response = jsonify([planet.to_dict() for planet in planets])

    return planets_response


@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_id(Planet, planet_id)
    return planet.to_dict()


@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_id(Planet, planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.surface_area = request_body["surface_area"]
    planet.moons = request_body["moons"]
    planet.distance_from_sun = request_body["distance_from_sun"]
    planet.namesake = request_body["namesake"]

    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully updated")


@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_one_planet(planet_id):
    planet = validate_id(Planet, planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully deleted")
