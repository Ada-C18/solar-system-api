from unicodedata import name
from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet

# class Planet:

#     def __init__(self, id, name, description, moons):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.moons = moons

# planets = [
#     Planet(1, "Earth", "our home", 1),
#     Planet(2, "Mars", "red planet", 2),
#     Planet(3, "Pluto", "is a planet", 5)
# ]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def create_planet():
    if request.method == "POST":
        request_body = request.get_json()
        if ("name" not in request_body or "description" not in request_body
        or "moons" not in request_body):
            return make_response(f"Invalid Request", 400)
        
        new_planet = Planet(
            name=request_body["name"],
            description=request_body["description"],
            moons=request_body["moons"],
        )

        db.session.add(new_planet)
        db.session.commit()

        return make_response(
            f"Planet {new_planet.name} successfully created", 201
        )

@planets_bp.route("", methods=["GET"])
def read_all_planets():
    planets_response = []
    planets = Planet.query.all()
    for planet in planets:
    #     planets_response.append({
    #         "id": planet.id,
    #         "name": planet.name,
    #         "description": planet.description,
    #         "moons": planet.moons
    # })
        planets_response.append(planet.to_dict())
    return jsonify(planets_response)

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"planet {planet_id} is invalid"}, 400))
    
    planet = Planet.query.get(planet_id)
    
    if not planet:
        abort(make_response({"message": f"planet {planet_id} not found"}, 404))
    
    return planet

@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return planet.to_dict()
    # return {
    #     "id": planet.id,
    #     "name": planet.name,
    #     "description": planet.description,
    #     "moons": planet.moons,
    # }

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    
    request_body = request.get_json()
    
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.moons = request_body["moons"]
    
    db.session.commit()
    
    return make_response(f"Planet #{planet.id} successfully updated")

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully deleted")