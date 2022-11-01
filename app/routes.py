from app import db 
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request, abort 


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def add_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                    description=request_body["description"],
                    diameter=request_body["diameter"]
                    )

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("", methods=["GET"])
def read_all_planets():
    planets_response = []
    planets = Planet.query.all()
    for planet in planets:
        planets_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "diameter": planet.diameter
            }
        )
    return jsonify(planets_response) 

def validate_planet(planet_id):
    try: 
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"planet {planet_id} invalid"}, 400)) 

    planet = Planet.query.get(planet_id)
    
    if not planet:
        abort(make_response({"message": f"planet {planet_id} not found"}, 404)) 

    return planet

@planets_bp.route("/<planet_id>", methods = ["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(planet_id)
    
    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "diameter": planet.diameter
    }

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.diameter = request_body["diameter"]


    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully updated")

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully deleted")

# class Planets(): 
#     def __init__(self, id, name, description, diameter): 
#         self.id = id
#         self.name = name 
#         self.description = description 
#         self.diameter = diameter 

# PLANETS = [
#     Planets(1, "Mercury", "closest planet to the sun", "3032 miles"), 
#     Planets(2, "Venus", "hottest planet", "7521 miles"), 
#     Planets(3, "Earth", "round and trashy", "7917 miles"),
#     Planets(4, "Mars", "reddish hue", "4212 miles"), 
#     Planets(5, "Jupiter", "largest planet", "86881 miles"), 
#     Planets(6, "Saturn", "surrounded by rings", "72367 miles"), 
#     Planets(7, "Uranus", "coldest planet", "31518 miles"), 
#     Planets(8, "Neptune", "most windy planet", "30599 miles"), 
# ]




    










