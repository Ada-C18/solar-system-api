from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    moon_count = db.Column(db.Integer)

    def to_dict(self):
        planet_dict = {}
        planet_dict["id"] = self.id
        planet_dict["name"] = self.name
        planet_dict["description"] = self.description
        planet_dict["moon_count"] = self.moon_count

        return planet_dict

    @classmethod
    def from_dict(cls, req_body):
        return cls(
            name=req_body["name"],
            description= req_body["description"],
            moon_count= req_body["moon_count"]
        )

    def update(self, req_body):
        self.name = req_body["name"]
        self.description = req_body["description"]
        self.moon_count = req_body["moon_count"]