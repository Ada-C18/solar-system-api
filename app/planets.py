from flask import Blueprint,jsonify


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
    # for planet in Planets_list:
    
        # planet_response.append({
        #     "id": planet.id,
        #     "name": planet.name,
        #     "color": planet.color,
        #     "description": planet.description

        #     })


    return jsonify(planet_response)
