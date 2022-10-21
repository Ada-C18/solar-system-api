from flask import Blueprint


class Planet:
    def __init__(self, id, name, description, mass):
        self.id = id
        self.name = name
        self.description = description
        self.mass = mass


list_of_planets = [
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
def handle_planets():
    return "Planets", 201


@planet_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    return f"Planet {planet_id}", 201
