from flask import Blueprint,jsonify,abort,make_response



class Planets:
    def __init__(self, id, name, color, description):
        self.id = id
        self.name = name
        self.color = color
        self.description = description

Planets_list = [
    Planets(1, 'Dink', 'Green', 'Fluffy'), 
    Planets(2, 'Blorp', 'Purple', 'Stinky'),
    Planets(3, 'Florpus', 'Red', 'Shy')
    ]

planets_bp = Blueprint('planets_bp', __name__, url_prefix='/planets')

@planets_bp.route('', methods=['GET'])
def get_all_planets():
    planet_response = [vars(planet) for planet in Planets_list]

    return jsonify(planet_response)

@planets_bp.route('/<id>', methods=['GET'])
def get_one_planet(id):
    # planet_id = int(id)
    # for planet in Planets_list:
    #     if planet.id == planet_id:
    #         return vars(planet)
    planet_id = validate_planet(id)
    return planet_id

def validate_planet(id):
    try:
        planet_id = int(id)
    except ValueError:
        return {
            "message": 'invalid id'
        }, 400

    for planet in Planets_list:
        if planet.id == planet_id:
            return vars(planet)

    
    abort(make_response(jsonify(description ="Resource not found"),404))