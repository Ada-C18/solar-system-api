from os import abort
from app.models.planet import Planet
from app import db
from flask import Blueprint, jsonify, make_response, abort, request


# class Planet:
#     def __init__(self, id, name, description, miles_from_sun):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.miles_from_sun = miles_from_sun
    
#     def to_json(self):
#         return dict(
#             id=self.id,
#             name=self.name,
#             description=self.description,
#             miles_from_sun = self.miles_from_sun
#         )

# planets = [
#     Planet(1, "Mercury", "The smallest planet in the Solar System and the closest to the Sun", "36.04 million"),
#     Planet(2, "Venus", "The second planet from the Sun. It is sometimes called Earth's sister or twin planet as it is almost as large and has a similar composition", "67.24 million"),
#     Planet(3, "Earth", "The fifth largest planet in the solar system, it is the only world in our solar system with liquid water on the surfac", "92.96 million"),
#     Planet(4, "Mars", "The fourth planet from the Sun and the second-smallest planet in the Solar System", "141.6 million"),
#     Planet(5, "Jupiter", "The largest in the Solar System. It is a gas giant with a mass more than two and a half times that of all the other planets in the Solar System combined", "483.8 million"),
#     Planet(6, "Saturn", "The sixth planet from the Sun and the second-largest in the Solar System", "890.8 million"),
#     Planet(7, "Uranus", "The seventh planet from the Sun. Its name is a reference to the Greek god of the sky, Uranus", "1.784 billion"),
#     Planet(8, "Neptune", "The eighth planet from the Sun and the farthest known solar planet. ", "2.793 billion")
# ]

bp = Blueprint("planets", __name__, url_prefix="/planets")


@bp.route("", methods=["POST"])
def handle_planets():
    request_body = request.get_json()
    new_planet = Planet(title=request_body["title"],
                    description=request_body["description"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.title} successfully created", 201)
# @bp.route("", methods=["GET"])
# def handle_planets():
#     planets_response = []
#     for planet in planets:
#         planets_response.append(planet.to_json())
#     return jsonify(planets_response)


# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)

#     except:
#         abort(make_response({"message":f"planet{planet_id} invalid"}, 400)) 
    
#     for planet in planets:
#         if planet.id == planet_id:
#             return planet

#     abort(make_response({"message": f"planet{planet_id} not found"}, 404))

# @bp.route("/<id>", methods=["GET"])
# def handle_planet(id):
#     planet = validate_planet(id)
#     return jsonify(planet.to_json())