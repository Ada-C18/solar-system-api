from app import db


class Planet(db.Model):  # The class Planet inherits from db.Model from SQLAlchemy
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    temperature = db.Column(db.Integer, nullable=False)

    @classmethod
    def from_dict(cls, data_dict):
        return cls(name=data_dict["name"], description=data_dict["description"], temperature=data_dict["temperature"])

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            temperature=self.temperature
        )
    