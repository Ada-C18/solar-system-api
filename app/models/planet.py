from app import db


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    surface_area = db.Column(db.BigInteger)
    moons = db.Column(db.Integer)
    distance_from_sun = db.Column(db.BigInteger)
    namesake = db.Column(db.String)

    def to_dict(self):
        return {
            "name": self.name,
            "surface_area": self.surface_area,
            "moons": self.moons,
            "distance_from_sun": self.distance_from_sun,
            "namesake": self.namesake,
        }

    @classmethod
    def create_from_json(cls, req_body):
        return cls(
            name=req_body["name"],
            surface_area=req_body["surface_area"],
            moons=req_body["moons"],
            distance_from_sun=req_body["distance_from_sun"],
            namesake=req_body["namesake"],
        )
