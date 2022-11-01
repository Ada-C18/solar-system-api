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

@bp.route('', methods=["GET"])
def read_all_planets():
    planets_databases = []
    planets = Planet.query.all()
    for planet in planets:
        planets_databases.append(planet.to_dict())
    return jsonify(planets_databases)

def validate_planet(id):
    try:
        planet_id = int(id)
    except:
        abort(make_response({"message": f"{id} is invalid"}, 400))
    planet = Planet.query.get(id)
    if not planet:
        abort(make_response({"message": f"{id} not found"}, 404))
    return planet


@bp.route('/<id>', methods=['GET'])
def read_one_planet(id):
    planet = validate_planet(id)
    return jsonify(planet.to_dict())

@bp.route('/<id>', methods=['PUT'])
def update_planet(id):
    planet = validate_planet(id)
    request_body = request.get_json()
    planet.name = request_body['name']
    planet.description = request_body['description']
    planet.radius = request_body['radius']
    db.session.commit()
    
    return make_response(f'planet {planet.name}: sucessfully updated', 200)


@bp.route('/<id>', methods=['DELETE'])
def delete_planet(id):
    planet = validate_planet(id)
    db.session.delete(planet)
    db.session.commit()
    return make_response(f'planet {planet.name}: sucessfully deleted', 200)


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



# @bp.route('<id>', methods=["GET"])
# def get_planet(id):
#     planet=validate_planet(id)
#     return planet.retrieve_planet()
    
