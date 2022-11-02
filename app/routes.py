from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet

# class Planet:
#     def __init__(self, id, name, description, flag):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.flag = flag

# planets = [ 
# Planet(0, "jupiter", "largest planet in solar system", False),
# Planet(1, "mercury", "smallest planet in solar system", False), 
# Planet(2, "mars", "most explored planet in solar system", True)
# ]

planet_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planet_bp.route("", methods=["GET", "POST"])
def handle_planets():
    if request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(name=request_body["name"], 
                            description=request_body["description"],
                            flag=request_body["flag"])
        db.session.add(new_planet)
        db.session.commit()
        return make_response("yay!", 201)
    elif request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        planets_response.append([planet.to_dict() for planet in planets])
        return jsonify(planets_response)


def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message": f"object {model_id} is invalid"}, 400))
    
    model = cls.query.get(model_id)
    if not model:
        abort(make_response({"message": f"{model_id} not found"}, 404))


@planet_bp.route("/<id>", methods=["GET"])
def get_planet(id):
    validate_model(Planet, id)
    planet = Planet.query.get(id)
    return jsonify(planet.to_dict())


# @planet_bp.route("", methods=["GET"])
# def list_planets():
#     planet_list = []
#     for planet in planets:
#         planet_list.append(dict(
#         id = planet.id,
#         name = planet.name,
#         description = planet.description,
#         flag = planet.flag
#         ))
#     return jsonify(planet_list)

# @planet_bp.route("/<id>", methods=["GET"])
# def get_planet(id):
#     planet = validate_planet(id)
#     return jsonify(dict(
#         id = planet.id,
#         name = planet.name,
#         description = planet.description,
#         flag = planet.flag,
#     ))

# def validate_planet(id):
#     try:
#         planet_id = int(id)
#     except:
#         abort(make_response({"message": f"planet {id} is invalid"}, 400))
#     for planet in planets:
#         if planet.id == planet_id:
#             return planet
#     abort(make_response({"message": f"{planet_id} not found"}, 404))