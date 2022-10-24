from crypt import methods
from os import abort
from flask import Blueprint,jsonify,abort,make_response

class Planet:
    def __init__(self,id,name,eq_diam,mass,moons,description):
        self.id = id
        self.name = name
        self.eq_diam = eq_diam
        self.mass = mass
        self.moons = moons
        self.description = description
    
        

PLANETS =[
    
    Planet(1, "Mercury",0.383,0.06,0,"the smallest planet in our solar system and closest to the Sun—is only slightly larger than Earth's Moon. Mercury is the fastest planet, zipping around the Sun every 88 Earth days"),
    Planet(2, "Venus",0.949,0.81,0,"Venus spins slowly in the opposite direction from most planets. A thick atmosphere traps heat in a runaway greenhouse effect, making it the hottest planet in our solar system"),
    Planet(3, "Earth",1.000,1.00,1,"our home planet—is the only place we know of so far that’s inhabited by living things. It's also the only planet in our solar system with liquid water on the surface" )
    ]        
planets_bp = Blueprint('planets_bp', __name__, url_prefix='/planets')  

@planets_bp.route('',methods=['GET'])
def get_all_planets():
    planet_response = [vars(planet) for planet in PLANETS]
    return  jsonify(planet_response) 
    # for planet in PLANETS:
    #     planet_response.append({
    #         'id': planet.id,
    #         'name': planet.name,
    #         'eq_diam': planet.eq_diam,
    #         'mass': planet.mass,
    #         'moons': planet.moons,
    #         'deskriptions': planet.description

    #     })

@planets_bp.route('/<id>',methods=['GET'])
def get_one_planet(id):
    planet = validate_planet(id)
    return planet

def validate_planet(id):
    try:
        planet_id = int(id)
    except ValueError:
        return {
            'message': 'Invalid planer id'
        },400
    for planet in PLANETS:
        if planet.id == planet_id:
            return vars(planet)
    abort(make_response(jsonify(description = 'Resourse not found'),404))
    # print(type(planet_response))
    # print(type(jsonify(planet_response)))
    