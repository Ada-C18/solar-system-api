from flask import Blueprint


class Planets(): 
    def __init__(self, id, name, description, diameter): 
        self.id = id
        self.name = name 
        self.description = description 
        self.diameter = diameter 

PLANETS = [
    Planets(1, "Mercury", "closest planet to the sun", "3032 miles"), 
    Planets(1, "Venus", "hottest planet", "7521 miles"), 
    Planets(1, "Earth", "round and trashy", "7917 miles"),
    Planets(1, "Mars", "reddish hue", "4212 miles"), 
    Planets(1, "Jupiter", "largest planet", "86881 miles"), 
    Planets(1, "Saturn", "surrounded by rings", "72367 miles"), 
    Planets(1, "Uranus", "coldest planet", "31518 miles"), 
    Planets(1, "Neptune", "most windy planet", "30599 miles"), 
]