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