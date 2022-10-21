# tell flask you want to import data
from unicodedata import name
from flask import Blueprint

class Planet:

    def __init__(self, id, name, description, color):
        self.id = id
        self.name = name
        self.description = description
        self.color = color

planet_1 = Planet(1, "Planet 1", "small and round", "blue")
planet_2 = Planet(2, "Planet 2", "big and bouncy", "red")
planet_3 = Planet(3, "Planet 3", "wispy", "green")

PLANET_LIST = [
    planet_1,
    planet_2,
    planet_3
]


# As a client, I want to send a request...

# 1. ...to get one existing `planet`, so that I can see the `id`, `name`, 
# `description`, and other data of the `planet`.
# 1. ... such that trying to get one non-existing `planet` responds 
# with get a `404` response, so that I know the `planet` resource 
# was not found.
# 1. ... such that trying to get one `planet` with an invalid 
# `planet_id` responds with get a `400` response, so that I know 
# the `planet_id` was invalid.