from flask import Blueprint, jsonify, abort, make_response
import json


class Planet:
    def __init__(self, id, name, description, temperature):
        self.id = id
        self.name = name
        self.description = description
        self.temperature = temperature

    def to_planet_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            temperature=self.temperature
        )


planets = [
    Planet(1, 'Mercury', 'Grey', '333˚F(167˚C)'),
    Planet(2, 'Venus', 'yellow-white', '967˚F(15°C)'),
    Planet(3, 'Earth', 'blue-green', '59˚F(15°C)'),
    Planet(4, 'Mars', 'red', '-85˚F(-65˚C')
]

bp = Blueprint("planets", __name__, url_prefix="/planets")


def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"planet {planet_id} not valid"}, 400))
    for planet in planets:
        if planet.id == planet_id:
            return planet
    abort(make_response({"message": f"planet {planet_id} not found"}, 404))


@bp.route("", methods=["GET"])
def handle_planets():
    results_list = []
    for planet in planets:
        results_list.append(planet.to_planet_dict())
    return jsonify(results_list)


@bp.route("/<planet_id>", methods=["GET"])
def get_planet(planet_id):
    planet = validate_planet(planet_id)
    return jsonify(planet.to_planet_dict())
