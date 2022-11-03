from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    miles_from_sun = db.Column(db.String)

    def to_dict(self):
        planet_as_dict = {}
        planet_as_dict["id"] = self.id
        planet_as_dict["name"] = self.name
        planet_as_dict['description'] = self.description
        planet_as_dict["miles from sun"] = self.miles_from_sun

        return planet_as_dict

    @classmethod
    def from_dict(cls, planet_data):
        new_planet = Planet(name=planet_data["name"], description=planet_data["description"], miles_from_sun=["miles from sun"])
        return new_planet