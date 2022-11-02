from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    color = db.Column(db.String)

def to_dict(self):
    planet_as_dict = {}
    planet_as_dict["id"] = self.id, 
    planet_as_dict["name"] = self.name, 
    planet_as_dict["description"] = self.description,
    planet_as_dict["color"] = self.color
    
    return planet_as_dict

@classmethod
