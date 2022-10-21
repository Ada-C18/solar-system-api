from flask import Blueprint

class Planet:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

mercury = Planet(1, "Mercury", "smallest planet")
venus = Planet(2, "Venus", "hottest planet")
earth = Planet(3, "Earth", "only planet known to harbor intelligent life")
mars = Planet(4, "Mars", "most likely planet to terraform")
jupiter = Planet(5, "Jupiter", "largest planet")
saturn = Planet(6, "Saturn", "only planet with a ring system")
uranus = Planet(7, "Uranus", "only planet with an almost vertical equator")
neptune = Planet(8, "Neptune", "coldest planet")
pluto = Planet(9, "Pluto", "only planet to be disowned fromt the Solar System")

solar_system = [
    mercury,
    venus,
    earth,
    mars,
    jupiter,
    saturn,
    uranus,
    neptune,
    pluto
]

