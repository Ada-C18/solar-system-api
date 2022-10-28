from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet


bp = Blueprint('planets', __name__, url_prefix='/planets')


@bp.route('', methods=['POST'])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body['name'],
            description = request_body['description'],
            radius = request_body['radius'])
    db.session.add(new_planet)
    db.session.commit()
    return make_response(f'Planet: {new_planet.name} succesfully created'), 201




# class Planet:
#     def __init__(self, id, name, description, radius):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.radius = radius
#     def retrieve_planet(self):
#         return dict(id=self.id, name=self.name, description=self.description, radius=self.radius)

# planets = [
#     Planet(1, 'Earth', 'good place', 6371 ), 
#     Planet(2, 'Jupiter', 'fun place', 69901),
#     Planet(3, 'Mars', 'weird place', 3389.5)
# ]

# bp = Blueprint('planets', __name__, url_prefix='/planets')
# @bp.route('', methods=["GET"])
# def get_planets():
#     planet_data = []
#     for planet in planets:
#         planet_data.append(planet.retrieve_planet())
#     return jsonify(planet_data)

# def validate_planet(id):
#     try:
#         planet_id = int(id)
#     except:
#         abort(make_response({"message": f"{id} is invalid"}, 400))
#     for planet in planets:
#         if planet_id == planet.id:
#             return(planet)
#     abort(make_response({"message": f"{id} not found"}, 404))

# @bp.route('<id>', methods=["GET"])
# def get_planet(id):
#     planet=validate_planet(id)
#     return planet.retrieve_planet()
    
