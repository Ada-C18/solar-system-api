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

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def read_all_planets():
    planets_response = []
    planets = Planet.query.all()
    for planet in planets:
        planets_response.append(dict(
            id=planet.id,
            name=planet.name,
            surface_area=planet.surface_area,
            moons=planet.moons,
            distance_from_sun=planet.distance_from_sun,
            namesake=planet.namesake
        ))

    return jsonify(planets_response)


@planets_bp.route("", methods=["POST"])        
def add_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                    surface_area=request_body["surface_area"], 
                    moons=request_body["moons"],
                    distance_from_sun=request_body["distance_from_sun"],
                    namesake=request_body["namesake"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully added", 201)