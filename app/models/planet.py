from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    rings = db.Column(db.Boolean, nullable=False)

    # have planet construct itself from passed in dict
    @classmethod
    def from_dict(cls, data_dict):
        return cls(name=data_dict["name"],
            description=data_dict["description"],
            rings=data_dict["rings"])

    def to_dict(self):
        return dict(
            id = self.id,
            name = self.name,
            description = self.description,
            rings = self.rings)