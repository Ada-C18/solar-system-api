from flask import Blueprint, jsonify, abort, make_response
from .models.planet import Planet

bp = Blueprint("planets", __name__, url_prefix="/planets")


def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"planet {planet_id} invalid"}, 400))

    for planet in planets:
        if planet.id == planet_id:
            return planet

    abort(make_response({"message": f"planet {planet_id} not found"}, 404))


@bp.route("", methods=["GET"])
def handle_planets():
    planet_list = []
    for planet in planets:
        planet_list.append(planet.to_dict())
    return jsonify(planet_list)


@bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planet = validate_planet(planet_id)

    return jsonify(planet.to_dict())
