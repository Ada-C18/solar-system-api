from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request 



bp = Blueprint("planets", __name__, url_prefix="/planet")


# @bp.route("", methods=["GET"])
# def handle_planets():
#     planets_list = []
#     for planet in planet_list:
#         planets_list.append(planet.to_dict())
#     return jsonify(planets_list)


def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message":f"planet {planet_id} not found"}, 404))

    return planet

# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"message": f"{planet_id} is not valid"}, 400))

#     for planet in planet_list:
#         if planet.id == planet_id:
#             return jsonify(planet.to_dict())
#     abort(make_response({"message": f"{planet_id} is not found"}, 404))


# @bp.route("/<planet_id>", methods=["GET"])
# def handle_planet(planet_id):
#     result_planet = validate_planet(planet_id)
#     return result_planet


@bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(# id=request_body["id"],
                        name=request_body["name"],
                        description=request_body["description"],
                        distance=request_body["distance"])
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Plaent {new_planet.name} successfully created", 201)

@bp.route("", methods=["GET"])
def read_all_planets():
    planets = Planet.query.all()
    planets_response = [planet.to_dict() for planet in planets]
    
    return jsonify(planets_response)
