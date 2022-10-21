from flask import Blueprint


class Planets(): 
    def __init__(self, id, name, description, diameter): 
        self.id = id
        self.name = name 
        self.description = description 
        self.diameter = diameter 

PLANETS = [Planets(1, "Earth", "round and trashy", "unknown")] 