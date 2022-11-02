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

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"{cls.__name__} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)

    if not model:
        abort(make_response({"message":f"{cls.__name__} {model_id} not found"}, 404))

    return model

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def handle_planet():
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("", methods=["GET"])
def read_all_planets():

    name_query = request.args.get("name")
    if name_query:
        planet = Planet.query.filter_by(name=name_query)
    else:
        planet = Planet.query.all()


    planet_response = [planet.to_dict() for planet in planet]

    return jsonify(planet_response)

    # planet = Planet.query.all()
    # for planet in planet:
    #     planet_response.append(planet.to_dict())
    # return jsonify(planet_response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    return planet.to_dict()

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.radius = request_body["radius"]

    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully updated")


@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully deleted")