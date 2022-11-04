from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

# INSTANIATE BLUEPRINT FOR ROUTES
planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response(
            {"message": f"{cls.__name__} {model_id} invalid"}, 400))

    planet = cls.query.get(model_id)

    if not planet:
        abort(make_response(
            {"message": f"{cls.__name__} {model_id} can't be found"}, 404))

    return planet


@planets_bp.route("/", strict_slashes=False, methods=["POST"])
def create_planet():

    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return make_response(jsonify(f"Planet {new_planet.name} successfully created"), 201)


@planets_bp.route("/", strict_slashes=False, methods=["GET"])
def read_all_planets():
    name_query = request.args.get("name")
    description_query = request.args.get("description")
    temperature_query = request.args.get("temperature")

    planet_query = Planet.query  # like SELECT * from planets

    if name_query:
        planet_query = planet_query.filter_by(name=name_query)  # ask Isabella

    if description_query:
        planet_query = planet_query.filter_by(description=description_query)

    if temperature_query:
        planet_query = planet_query.filter_by(temperature=temperature_query)

    planets = planet_query.all()

    planet_response = [planet.to_dict() for planet in planets]

    return jsonify(planet_response)


@planets_bp.route("/<id>", strict_slashes=False, methods=["GET"])
def read_one_planet(id):

    planet = validate_model(Planet, id)
    return planet.to_dict(), 200


@planets_bp.route("/<id>", strict_slashes=False, methods=["PUT"])
def update_planet(id):

    planet = validate_model(Planet, id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.temperature = request_body["temperature"]

    db.session.commit()
    return make_response(jsonify(f"Planet #{planet.id} successfully updated"), 200)


@planets_bp.route("/<id>", methods=["DELETE"])
def delete_planet(id):

    planet = validate_model(Planet, id)
    db.session.delete(planet)
    db.session.commit()
    return make_response(jsonify(f"Planet #{planet.id} successfully deleted"), 200)
