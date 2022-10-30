from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"book {planet_id} invalid"}, 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message":f"planet {planet_id} not found"}, 404))

    return planet


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
    name_query = request.args.get("name")
    if name_query:
        planets = Planet.query.filter_by(name=name_query)
    else:
        planets = Planet.query.all()

    planets_response = []
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

@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_book(planet_id):
    planet = validate_planet(planet_id)
    return {
            "name" : planet.name,
            "surface_area": planet.surface_area,
            "moons": planet.moons,
            "distance_from_sun": planet.distance_from_sun,
            "namesake": planet.namesake
        }


@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.surface_area = request_body["surface_area"]
    planet.moons = request_body["moons"]
    planet.distance_from_sun = request_body["distance_from_sun"]
    planet.namesake = request_body["namesake"]

    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully updated")


@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_one_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully deleted")