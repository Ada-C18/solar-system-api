from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    color = db.Column(db.String)
    livability = db.Column(db.Integer)
    moons = db.Column(db.Integer)
    is_dwarf = db.Column(db.Boolean)

    def to_dict(self):
        planet_as_dict = {}
        planet_as_dict["id"] = self.id
        planet_as_dict["name"] = self.name
        planet_as_dict["color"] = self.color
        planet_as_dict["livability"] = self.livability
        planet_as_dict["moons"] = self.moons
        planet_as_dict["is_dwarf"] = self.is_dwarf
        return planet_as_dict

    @classmethod
    def from_dict(cls, planet_data):
        new_planet = Planet(name=planet_data["name"],
            color=planet_data["color"],
            moons=planet_data["moons"],
            livability=planet_data["livability"],
            is_dwarf=planet_data["is_dwarf"])
        return new_planet