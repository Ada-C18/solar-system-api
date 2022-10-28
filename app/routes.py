from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request

planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

@planet_bp.route("", methods=["POST"])
def handle_planets():
    request_body = request.get_json()
    planet_1 = Planet(
        name = request_body["name"], 
        description = request_body["description"],
        moons = request_body["moons"])

    db.session.add(planet_1)
    db.session.commit()

    return make_response(f"Planet {planet_1.name} successfully created", 201)

# @planet_bp.route("", methods = ["GET"])
# def read_planets():
#     return return_all_planets()

# @planet_bp.route("/<planet_id>", methods=["GET"])
# def handle_planet(planet_id):
#     return verify_planet(planet_id) 
