from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                    surface_area=request_body["surface_area"], 
                    moons=request_body["moons"],
                    distance_from_sun=request_body["distance_from_sun"],
                    namesake=request_body["namesake"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

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