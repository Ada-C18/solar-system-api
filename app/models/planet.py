from app import db


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    moons = db.Column(db.Integer)

    def to_dict(self):
        planet_to_dict = {}
        planet_to_dict["id"] = self.id
        planet_to_dict["name"] = self.name
        planet_to_dict["description"] = self.description
        planet_to_dict["moons"] = self.moons

        return planet_to_dict