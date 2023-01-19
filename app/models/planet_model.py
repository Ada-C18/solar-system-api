from app import db

# Create the class that is inherited from the db.Model from SQLAlchemy
class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    rings = db.Column(db.Integer)