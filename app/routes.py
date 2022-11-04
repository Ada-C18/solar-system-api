from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"{cls.__name__} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)

    if not model:
        abort(make_response({"message":f"{cls.__name__} {model_id} not found"}, 404))

    return model

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def create_new_planet():
    request_body = request.get_json(force=True)
    new_planet = Planet.from_dict(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("", methods=["GET"])
def read_all_planets():

    name_query = request.args.get("name")
    if name_query:
        planets = Planet.query.filter_by(name=name_query)
    else:
        planets = Planet.query.all()
    planets_response = []
    
    for planet in planets:
        planets_response.append(planet.to_dict())
    return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    return planet.to_dict()


# @planets_bp.route("", methods=["GET"])
# def show_all_planets():
#     planets_response = []
#     for planet in list_of_planets:
#         planets_response.append({
#             "id": planet.id,
#             "name": planet.name,
#             "description": planet.description,
#             "number of moons": planet.moons 
#         })
#     return jsonify(planets_response)

# @planets_bp.route("/<planet_id>", methods=["GET"])
# def get_planet_info(planet_id):
#     planet = validate_planet(planet_id)
#     return {
#         "id": planet.id,
#         "name": planet.name,
#         "description": planet.description,
#         "number of moons": planet.moons
#     }

