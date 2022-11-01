from app import db
from models.planet import Planet 
from flask import Blueprint, jsonify, abort, request, make_response

# class Planet():
#     def __init__(self, id, name):#removed description and moon_count for now
#         self.id = id
#         self.name = name
#         # self.description = description
#         # self.moon_count = moon_count

# PLANETS = [
#     Planet(1, "Mercury"),
#     Planet(2, "Venus"),
#     Planet(3, "Mars"),
#     Planet(4, "Earth"),
#     Planet(5, "Jupiter"),
#     Planet(6, "Saturn"),
#     Planet(7, "Uranus"),
#     Planet(8, "Neptune")
# ]
# HELPER FUNCTIONS #

def validate_planet(planet_id): 
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"{planet_id} is invalid"}, 400))
    
    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message": f"planet {planet_id} not found"}, 404))

    return planet

# ROUTE FUNCTIONS # 

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    if "name" not in request_body or "description" not in request_body or "moon_count" not in request_body:
        return make_response("Invalid Request", 400)
    new_planet = Planet(
        name = request_body["name"],
        description = request_body["description"],
        moon_count = request_body["moon_count"]
    )

    db.session.add(new_planet)
    db.session.commit()
    return make_response(f" Planet {new_planet.name} sucessfully created", 201)

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    all_planets = Planet.query.all()
    # results_list = [{"name": planet.name, "description": planet.description, "moon count": planet.moon_count} for planet in all_planets]
    results_list = []
    for planet in all_planets:
        results_list.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "moon_count": planet.moon_count
        })
    return jsonify(results_list), 200

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()


    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.moon_count = request_body["moon_count"]

    db.session.commit()
    return make_response("Planet {planet.id} successfully updated")

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return {"id": planet.id,
            "name": planet.name,
            "description": planet.description, 
            "moon_count": planet.moon_count
    }

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)
    
    db.session.delete(planet)
    db.session.commit()

    return make_response("Book #{planet_id} successfully deleted")