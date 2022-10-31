from app import db 
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request 


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def handle_planets():
    request_body = request.get_json()
    new_planet = Planet(id=request_body["id"],
                    name=request_body["name"],
                    description=request_body["description"],
                    diameter=request_body["diameter"]
                    )

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("", methods=["GET"])
def read_all_planet():
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


# @planets_bp.route("", methods=["GET"])
# def handle_planets():
#     planets_response = []
#     for planet in PLANETS:
#         planets_response.append({
#             "id": planet.id,
#             "name": planet.name,
#             "description": planet.description,
#             "diameter": planet.diameter
#         })
#     return jsonify(planets_response)

# @planets_bp.route("/<planet_id>", methods = ["GET"])
# def handle_one_planet(planet_id):
#     planet = validate_planet(planet_id)
    
#     return {
#         "id": planet.id,
#         "name": planet.name,
#         "description": planet.description,
#         "diameter": planet.diameter
#     }

    


# def validate_planet(planet_id):
#     try: 
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"message": f"planet {planet_id} invalid"}, 400)) 

#     for planet in PLANETS:
#         if planet.id == planet_id:
#             return planet 
    
#     abort(make_response({"message": f"planet {planet_id} not found"}, 404)) 








