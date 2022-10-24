from unicodedata import name
from flask import Blueprint, jsonify


class Planet:
    def __init__(self,id,name,description,color):
        self.id = id
        self.name = name
        self.description = description
        self.color = color
planets = [
    Planet(1,"Earth","big","blue/green"),
    Planet(2,"Mars","smaller","red"),
    Planet(3,"Venus","a little bigger","gold")
]
bp = Blueprint("planets", __name__, url_prefix="/planets")
@bp.route("", methods=["GET"])
def handle_planets():
    all_planets = []
    for planet in planets:
        all_planets.append(dict(
            id= planet.id,
            name = planet.name,
            description = planet.description,
            color = planet.color

        ))
    return jsonify(all_planets)

@bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    try:
      planet_id = int(planet_id)
    except:
      return {"message":f"planet {planet_id} invalid"}, 400

    for planet in planets:
        if planet.id == planet_id:
            return {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "color": planet.color
            }
    return {"message":f"planet {planet_id} not found"}, 404

    


