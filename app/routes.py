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
    Planets(1, "earth", "green", 10),
    Planets(2, "venus", "orange", 5),
    Planets(3, "mars", "red", 7),
    Planets(4, "jupiter", "beige", 1),
    Planets(5, "neptune", "blue", 3),
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

