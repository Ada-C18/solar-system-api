from app import db


# MODELS are classes that inherit from db.Model from sqlalchemy
class Planet(db.Model): # defining the planet model
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String) # attribute title which will map to a db column
    description = db.Column(db.String)
    moons = db.Column(db.Integer)
