from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request


# planets = [
#     Planet(1,"Mercury","The smallest planet",1516),
#     Planet(2, "Venus","The second planet from the Sun and Earth's closest planetary neighbor",3760.4),
#     Planet(3, "Earth", "The third planet from the Sun and the only astronomical object known to harbor life",3958.8),
#     Planet(4, "Mars","The fourth planet from the Sun and the second-smallest planet in the Solar System, being larger than only Mercury",2106.1),
#     Planet(5, "Jupiter", "The fifth planet from the Sun and the largest in the Solar System",43441),
#     Planet(6, "Saturn", "The sixth planet from the Sun and the second-largest in the Solar System, after Jupiter",36184),
#     Planet(7, "Uranus", "The seventh planet from the Sun. Its name is a reference to the Greek god of the sky",15759),
#     Planet(8, "Neptune", "The eighth planet from the Sun and the farthest known solar planet",15299)
#     ]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def handle_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                    description=request_body["description"],
                    radius=request_body["radius"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("", methods=["GET"])
def read_all_planets():
    planet_response = []
    planet = Planet.query.all()
    for planet in planet:
        planet_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "radius": planet.radius
            }
        )
    return jsonify(planet_response)

