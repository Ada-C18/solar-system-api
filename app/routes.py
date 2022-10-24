from flask import Blueprint, jsonify
from sqlalchemy import desc

class Planet:
    def __init__(self, id, name, description):
        self.id = id
        self.name =  name
        self.description = description

# instance  = an instance of the object
jupiter = Planet(id=1, name = "Jupiter", description = "hmmm i think its a big planet")
mars = Planet(id= 2, name = "Mars", description="its close to the sun?")
mercury = Planet(id = 3, name = "Mercury", description="also close to the planet?")
venus = Planet(id= 4, name = "Venus", description = "this is aphrodite's planet?")
earth = Planet(id=5, name = "Earth", description = "us!")
saturn = Planet(id = 6, name = "Saturn", description = "this is the one with a lot of moons?")
uranus = Planet(id = 7, name = "Uranus", description="I know literally nothing about this one")
neptune = Planet(id = 8, name = "Neptune", description = "Poseidon's!")
pluto = Planet(id = 9, name = "Pluto", description = "dont forget about me!" )
list_of_planets = [jupiter, mars, mercury, venus, earth, saturn, uranus, neptune, pluto]

planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

@planet_bp.route("", methods = ["GET"])
def read_planets():
    planets_json = []
    for planet in list_of_planets:
        dict = {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description
        }
        planets_json.append(dict)
    return jsonify(planets_json)


@planet_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        return "Message: Invalid Planet.", 400

    for planet in list_of_planets:
        if planet.id == planet_id:
            return {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description
            }
    return "Message: Planet not found.", 404
        
