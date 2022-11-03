from app import db


# MODELS are classes that inherit from db.Model from sqlalchemy
class Planet(db.Model): # defining the planet model
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String) # attribute title which will map to a db column
    description = db.Column(db.String)
    moons = db.Column(db.Integer)

    def to_dict(self):
        return {
                "name": self.name,
                "description": self.description,
                "moons": self.moons,
                "id": self.id,
                }

    @classmethod
    def from_dict(cls, planet_data):
        planet_1 = Planet(
            name=planet_data["name"],
            description=planet_data["description"],
            moons=planet_data["moons"]
        )
        return planet_1