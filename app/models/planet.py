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

    @classmethod
    def from_dict(cls, planet_data):
        new_planet = Planet(name=planet_data["name"], description=planet_data["description"], moons=planet_data["moons"])
        return new_planet

    