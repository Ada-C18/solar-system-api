from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet

# class Planet():
#     def __init__(self, id, name, description, color):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.color = color

# PLANETS = [
#     Planet(1, "Saturn", "gassy giant", "orange"),
#     Planet(2, "Mercury", "small rocky", "gray"),
#     Planet(3, "Pluto", "still a planet", "white")
# ]

planet_bp = Blueprint("Planet", __name__, url_prefix="/planet")

@planet_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet.from_json(request_body)
    
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} has been created", 201)

@planet_bp.route("", methods=["GET"])
def get_all_planets():
    color_query = request.args.get("color")
    name_query = request.args.get("name")
    if color_query:
        all_planets = Planet.query.filter_by(color=color_query)
    elif name_query:
        all_planets = Planet.query.filter_by(name=name_query)
    else:
        all_planets = Planet.query.all()

    results_list = []
    # all_planets = Planet.query.all()

    for planet in all_planets:
        results_list.append(planet.to_dict())
    return jsonify(results_list), 200

@planet_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    planet = validate_id(Planet, planet_id)
    # planet = Planet.query.get(planet_id)

    return jsonify(planet.to_dict()), 200



@planet_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_id(Planet, planet_id)
    request_body = request.get_json()
    planet.update(request_body)
    db.session.commit()
    return make_response(f"Planet #{planet.id} successfully updated")

@planet_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_id(Planet, planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"planet #{planet.id} successfully deleted")



def validate_id(class_obj,id):
    try:
        id = int(id)
    except:
        abort(make_response({"message":f"{class_obj} {id} is an invalid id"}, 400))

    query_result = class_obj.query.get(id)
    if not query_result:
        abort(make_response({"message":f"{class_obj} {id} not found"}, 404))

    return query_result