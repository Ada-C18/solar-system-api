from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    moons = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return dict(
            id = self.id,
            name = self.name,
            description = self.description,
            moons = self.moons
            )