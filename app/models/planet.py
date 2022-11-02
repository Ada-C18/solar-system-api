from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    moons = db.Column(db.Integer)


    def to_dict(self):
        planet_as_dict = {}
        planet_as_dict["id"] = self.id
        planet_as_dict["name"] = self.name
        planet_as_dict["description"] = self.description

        return planet_as_dict
    
    def from_json(cls, req_body):
        return cls(
            name = req_body["name"],
            description = req_body["description"],
            moons = req_body["moons"]
        )