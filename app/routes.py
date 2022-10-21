from flask import Blueprint

class Planet():
    def __init__(self, id, name, description, moons):
        self.id = id
        self.name = name
        self.description = description
        self.moons = moons

list_of_planets = [
    Planet(1, "Mercury", "Grey smallest planet",0),
    Planet(2, "Venus", "Orange planet of love", 0),
    Planet(3, "Earth", "Our planet!", 1),
    Planet(4, "Mars", "Red planet that we're exploring", 2)
]