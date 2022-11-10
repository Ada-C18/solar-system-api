from app import db
from app.models.fictional_caretaker import Caretaker
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request
from app.routes.helper_functions import validate_model

bp = Blueprint("caretakers", __name__, url_prefix="/caretakers")

@bp.route("", methods=["POST"])
def create_caretaker():
    request_body = request.get_json()
    new_caretaker = Caretaker.from_dict(request_body)

    db.session.add(new_caretaker)
    db.session.commit()

    return make_response(f"Caretaker {new_caretaker.name} successfully created", 201)


@bp.route("", methods=["GET"])
def read_all_caretakers():
    caretakers = Caretaker.query.all()

    caretakers_response = [caretaker.to_dict() for caretaker in caretakers]

    return jsonify(caretakers_response)


@bp.route("/<caretaker_id>/planets", methods=["POST"])
def create_planet(caretaker_id):
    caretaker = validate_model(Caretaker, caretaker_id)
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)
    new_planet.caretaker = caretaker

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} cared for by {caretaker.name}", 201)


@bp.route("/<caretaker_id>/planets", methods=["GET"])
def read_one_planet(caretaker_id):
    caretaker = validate_model(Caretaker, caretaker_id)

    planet_response = [planet.to_dict() for planet in caretaker.planets]
  

    return(jsonify(planet_response))