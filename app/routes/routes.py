from flask import Blueprint, jsonify, abort, make_response

#created Planet class
class Planet:
    def __init__(self, id, name, description, moons):
        self.id = id
        self.name = name
        self.description = description
        self.moons = moons


    #method in class planet.to_planet
    def to_planet_dict(self):
        return dict(
            id=self.id, 
            name=self.name, 
            description=self.description,
            moons=self.moons
    )
#created planet instances
planets= [
    Planet(1, "fi", "red planet", 10),
    Planet(2, "fie", "blue planet", 9),
    Planet(3, "foo", "yellow planet", 8)
]
bp = Blueprint("planets", __name__, url_prefix="/planets") 
#call method .to planets, return jsonified result from dictionary
@bp.route("", methods=["GET"])
def handle_planets():
    results_list = []
    for planet in planets: 
                results_list.append(planet.to_planet_dict())
    return jsonify(results_list)

#validate input for request
def validate_planet(planet_id):
    #if string cannot cast to integer, return "bad request"
    try:
        planet_id= int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

    #if planet.id not found, return 404
    for planet in planets: 
        if planet.id == planet_id:
            return planet

    abort(make_response({"message":f"planet {planet_id} not found"}, 404))

#create endpoint blueprint
@bp.route("/<id>", methods=["GET"])
def handle_planet(id):
    planet = validate_planet(id)
    return jsonify(planet.to_planet_dict())