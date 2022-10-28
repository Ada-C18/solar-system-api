from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet


# class Planet:
#     def __init__(self,id,name,description,color):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.color = color

#     def to_json(self):
#         return dict(
#             id= self.id,
#             name = self.name,
#             description = self.description,
#             color = self.color)


# planets = [
#     Planet(1,"Earth","big","blue/green"),
#     Planet(2,"Mars","smaller","red"),
#     Planet(3,"Venus","a little bigger","gold")

bp = Blueprint("planets", __name__, url_prefix="/planets")
# @bp.route("", methods=["GET"])
# def handle_planets():
#     all_planets = []
#     for planet in planets:
#         all_planets.append(planet.to_json())
#     return jsonify(all_planets)

# def validate_planet(planet_id):
#     try:
#       planet_id = int(planet_id)
#     except:
#       abort(make_response({"message":f"planet {planet_id} invalid"}, 400))
    
#     for planet in planets:
#         if planet.id == planet_id:
#             return planet

#     abort(make_response({"message":f"planet {planet_id} not found"}, 404))
    


# @bp.route("/<planet_id>", methods=["GET"])
# def handle_planet(planet_id):
#     planet = validate_planet(planet_id)
#     return (planet.to_json())

    

@bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name = request_body["name"], 
    color = request_body["color"],
    description = request_body["description"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)



