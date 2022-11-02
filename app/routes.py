from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request, abort


# class Planet:
#     def __init__(self, id, name, description, num_moons):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.num_moons = num_moons


# PLANETS = [
#     Planet(1, 'Mercury', {"distance_from_sun": "36.04 million mi"}, 0),
#     Planet(2, 'Venus', {"distance_from_sun": "67.24 million mi"}, 0),
#     Planet(3, 'Earth', {"distance_from_sun": "92.96 million mi"}, 1),
#     Planet(4, 'Mars', {"distance_from_sun": "141.60 million mi"}, 2),
#     Planet(5, 'Jupiter', {"distance_from_sun": "483.80 million mi"}, 80),
#     Planet(6, 'Saturn', {"distance_from_sun": "890.8 million mi"}, 83),
#     Planet(7, 'Uranus', {"distance_from_sun": "1.784 billion mi"}, 27),
#     Planet(8, 'Neptune', {"distance_from_sun": "2.793 billion mi"}, 14),
#     Planet(9, 'Pluto', {"distance_from_sun": "3.70 billion mi"}, 5),
# ]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


@planets_bp.route("", methods=["GET"])
def read_planets():
    planet_query = Planet.query

    name_query = request.args.get("name")
    
    if name_query:
        planet_query = planet_query.filter_by(name=name_query)
        
    moon_query = request.args.get("num_moons")

    if moon_query:
        planet_query = planet_query.filter_by(num_moons=moon_query)

    planets_response = []
    planets = planet_query.all()  

    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "number of moons": planet.num_moons
        })
    
    if not planets_response:
        return make_response(jsonify(f"There are no planets named {name_query} planet"))
    
    return jsonify(planets_response)


@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                description=request_body["description"],
                num_moons=request_body["num_moons"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)



@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)
    
    return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "number of moons": planet.num_moons
            }


def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message":f"planet {planet_id} not found"}, 404))

    return planet


@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.num_moons = request_body["num_moons"]

    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully updated!")

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully deleted!")
