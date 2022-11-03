from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    distance_from_sun = db.Column(db.BigInteger, nullable=False)
    description = db.Column(db.String, nullable=False)

    @classmethod
    def from_dict(cls, data_dict):
        return cls(name=data_dict['name'], 
            distance_from_sun=data_dict['distance_from_sun'],
            description=data_dict['description'])

    def make_a_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "distance_from_sun": self.distance_from_sun,
            "description": self.description
        }