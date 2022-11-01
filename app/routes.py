from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request, abort


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

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message":f"planet {planet_id} not found"}, 404))

    return planet

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
        planet_response.append(planet.to_dict())
    return jsonify(planet_response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return planet.to_dict()

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.radius = request_body["radius"]

    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully updated")


@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully deleted")