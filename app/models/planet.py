from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    radius = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return dict(id = self.id, name = self.name, description = self.description, radius = self.radius)