from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    moons = db.Column(db.Integer, nullable=False)
    caretaker_id = db.Column(db.Integer, db.ForeignKey("caretaker.id"))
    caretaker = db.relationship("Caretaker", back_populates="planets")

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            moons=self.moons
    )

    @classmethod
    def from_dict(cls, data_dict):
        return cls(name=data_dict["name"],
        description=data_dict["description"],
        moons=data_dict["moons"])


