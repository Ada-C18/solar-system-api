from turtle import color
from unicodedata import name
from flask import Blueprint,jsonify

class Planets:
    def __init__(self, id, name, color, description):
        self.id = id
        self.name = name
        self.color = color
        self.description = description

    Planets = [
        Planets (1, 'Dink', 'Green', 'Fluffy'), 
        Planets (2, 'Blorp', 'Purple', 'Stinky'),
        Planets (3, 'Florpus', 'Red', 'Shy')
    ]

def get_all_planets():
    x = []
    for planet in Planets:
        x.append({
            "id": planet.id,
            "name": planet.name,
            "color": planet.color,
            "description": planet.description

            })


    return jsonify(x)
