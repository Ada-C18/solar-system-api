from flask import Blueprint , jsonify 

#create planet class
class Planets:
    def __init__(self, id, name, description, livability):
        self.id = id
        self.name = name
        self.description = description
        self.livability = livability

    # planet instances
planets = [
    Planets(3, "earth", "green terrestrial planet", 10.0),
    Planets(2, "venus", "orange terrestrial planet", 4.5),
    Planets(4, "mars", "red terrestrial planet", 7.9),
    Planets(5, "jupiter", "beige gas giant", 1.6),
    Planets(8, "neptune", "blue ice giant", 3.4),
    ]

planets_bp = Blueprint("planets", __name__, url_prefix = "/planets")
    
@planets_bp.route("", methods = ["GET"])
#get all planets, return as a lists with all attributes
def get_planets():
    planet_response = []
    for planet in planets:
        planet_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "livability": planet.livability
        })
    return jsonify(planet_response)

