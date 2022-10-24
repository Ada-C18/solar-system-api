from flask import Blueprint , jsonify, abort, make_response

class Planet:
    def __init__(self,id,name,description,radius):
        self.id = id
        self.name = name
        self.description = description
        self.radius = radius

planets = [
    Planet(1,"Mercury","The smallest planet",1516),
    Planet(2, "Venus","The second planet from the Sun and Earth's closest planetary neighbor",3760.4),
    Planet(3, "Earth", "The third planet from the Sun and the only astronomical object known to harbor life",3958.8),
    Planet(4, "Mars","The fourth planet from the Sun and the second-smallest planet in the Solar System, being larger than only Mercury",2106.1),
    Planet(5, "Jupiter", "The fifth planet from the Sun and the largest in the Solar System",43441),
    Planet(6, "Saturn", "The sixth planet from the Sun and the second-largest in the Solar System, after Jupiter",36184),
    Planet(7, "Uranus", "The seventh planet from the Sun. Its name is a reference to the Greek god of the sky",15759),
    Planet(8, "Neptune", "The eighth planet from the Sun and the farthest known solar planet",15299)
    ]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

def validate_planet_id(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"planet {planet_id} invalid"}, 400))

    for planet in planets:
        if planet.id == planet_id:
            return planet

    abort(make_response({"message": f"planet {planet_id} not found"}, 404))

@planets_bp.route("", methods=["GET"])
def handle_planets():
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "radius": planet.radius
        })
    return jsonify(planets_response), 200

@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planet = validate_planet_id(planet_id)
    
    return dict(
    id = planet.id,
    name = planet.name,
    description = planet.description,
    radius = planet.radius
    )