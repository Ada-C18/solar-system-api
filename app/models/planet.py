from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    distance_from_sun = db.Column(db.BigInteger, nullable=False)
    description = db.Column(db.String, nullable=False)

    def make_a_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "distance from sun": self.distance_from_sun,
            "description": self.description
        }

solar_system = [
    Planet(1, "Mercury", 35000000, "smallest planet"),
    Planet(2, "Venus", 67000000, "hottest planet"),
    Planet(3, "Earth", 93000000, "only planet known to harbor intelligent life"),
    Planet(4, "Mars", 142000000, "most likely planet to terraform"),
    Planet(5, "Jupiter", 484000000, "largest planet"),
    Planet(6, "Saturn", 889000000, "only planet with a ring system"),
    Planet(7, "Uranus", 1790000000, "only planet with an almost vertical equator"),
    Planet(8, "Neptune", 2880000000, "coldest planet"),
    Planet(9, "Pluto", 3670000000, "only planet to be disowned fromt the Solar System")
]