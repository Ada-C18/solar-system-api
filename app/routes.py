from flask import Blueprint, jsonify, make_response, request
from app.models.planet import Planet
from app import db

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body=request.get_json()
    new_planet = Planet(name = request_body["name"],
                description = request_body["description"],
                color = request_body["color"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("", methods=["GET"])
def read_all_planets():
    planets = Planet.query.all()
    planets_response = [planet.dict() for planet in planets]

    return jsonify(planets_response)