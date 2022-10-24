from flask import Blueprint


class Planet:
    def __init__(self, id, name, description, mass):
        self.id = id
        self.name = name
        self.description = description
        self.mass = mass
    
    def planet_dict(self):
        return self.id, {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "mass": self.mass
        }


planets = [
    #"Sol",
    Planet(1, "Mercury", "just a little guy", "small"),
    Planet(2, "Venus", "what a babe", "hot"),
    Planet(3, "Earth", "nice planet", "normal"),
    Planet(4, "Mars", "rude", "short king"),
    Planet(5, "Jupiter", "large and in charge", "mASSIVE"),
    Planet(6, "Saturn", "put a ring on it", "big enough"),
    Planet(7, "Uranus", "unacceptable in public", "normal i hope"),
    Planet(8, "Neptune", "frigid", "cant tell"),
]

planet_bp = Blueprint("planet", __name__, url_prefix="/planets")


@planet_bp.route("", methods=["GET"])
def handle_all_planets():
    all_planets = { p.id: p.planet_dict() for p in planets}
    return all_planets, 200


@planet_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    try:
        planet = planets[int(planet_id)-1]
    except ValueError:
        return {"error": "Invalid planet id"}, 400
    except IndexError:
        return {"error": "No planet by that id"}, 404
    #return f"Planet {planet.id}, {planet.name}, {planet.description}, {planet.mass}", 200
    return planet.planet_dict(), 200
