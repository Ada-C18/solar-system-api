from app import db
from flask import Blueprint, jsonify, abort, make_response, request
from .models.planet import Planet

bp = Blueprint("planets", __name__, url_prefix="/planets")


def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"planet {planet_id} invalid"}, 400))

    planets = Planet.query.all()
    for planet in planets:
        if planet.id == planet_id:
            return planet

    abort(make_response({"message": f"planet {planet_id} not found"}, 404))


@bp.route("", methods=["GET", "POST"])
def handle_planets():
    if request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append(planet.to_dict())
        return jsonify(planets_response)
    elif request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(
            # id=request_body["id"],
            name=request_body["name"], 
            description=request_body["description"],
            rings=request_body["rings"]
        )

        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"Planet {new_planet.name} successfully created", 201)


@bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planet = validate_planet(planet_id)

    return jsonify(planet.to_dict())
