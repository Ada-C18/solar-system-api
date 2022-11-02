from app import db
from flask import abort, make_response

class Planet(db.Model):
    id = db.Column(db.Integer,primary_key = True, autoincrement= True) 
    name = db.Column(db.String)
    description = db.Column(db.String)
    diameter = db.Column(db.String)

    def to_dict(self):
        return {
                "id": self.id,
                "name": self.name,
                "description": self.description,
                "diameter": self.diameter
                }

    @classmethod
    def from_dict(cls, planet_data):
        new_planet = Planet(name=planet_data["name"],
                        description=planet_data["description"],
                        diameter=planet_data["diameter"])
        return new_planet

    def update(self, req_body):
        try:
            self.name = req_body["name"]
            self.description = req_body["description"]
            self.diameter = req_body["diameter"]
        except KeyError as error:
            abort(make_response({"message": f"Missing attribute: {error}"}, 400))
    

