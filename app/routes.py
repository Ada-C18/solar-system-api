from flask import Blueprint

class Planet():
    def __init__(self, id, name, description, color):
        self.id = id
        self.name = name
        self.description = description
        self.color = color

PLANETS = [
    Planet(1, "Saturn", "gassy giant", "orange"),
    Planet(2, "Mercury", "small rocky", "gray"),
    Planet(3, "Pluto", "still a planet", "white")
]

planet_bp = Blueprint("Planet", __name__, url_prefix="/planet")



