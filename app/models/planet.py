from app import db


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    radius = db.Column(db.Integer)

    def to_dict(self):
        planet_as_dict = {}
        planet_as_dict["id"] = self.id
        planet_as_dict["name"] = self.name
        planet_as_dict["description"] = self.description
        planet_as_dict["radius"] = self.radius

        return planet_as_dict

    @classmethod
    def from_dict(cls, data_dict):
        return cls(name=data_dict["name"],
            description=data_dict["description"],
            radius=data_dict["radius"])
