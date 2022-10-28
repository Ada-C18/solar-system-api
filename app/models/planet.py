from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    color = db.Column(db.String)
    livability = db.Column(db.Integer)
    moons = db.Column(db.Integer)
    is_dwarf = db.Column(db.Boolean)