from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

# PLANETS = [
#     Planet(1, "Mercury", "closest to the sun", 0),
#     Planet(2, "Venus", "very high temps", 0),
#     Planet(3, "Earth", "home", 1),
#     Planet(4, "Mars", "the red planet", 2),
#     Planet(5, "Jupiter", "famous spot", 80),
#     Planet(6, "Saturn", "famous rings", 83),
#     Planet(7, "Uranus", "spins upside down", 27),
#     Planet(8, "Neptune", "furthest from the sun", 14),
# ]

planet_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planet_bp.route("", methods=["GET", "POST"])
def handle_planets():
    if request.method == "GET":
        planets = Planet.query.all()
        planet_response = []
        for planet in planets:
            planet_response.append({
                "name":planet.name,
                "description":planet.description,
                "moon": planet.moon,
                "id": planet.id
            })
        return jsonify(planet_response),200
        
    elif request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(
                        name=request_body["name"],
                        description=request_body["description"],
                        moon=request_body["moon"])

        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"Planet {new_planet.name} successfully added", 201)

