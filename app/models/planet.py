from app import db


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String, nullable = False)
    description = db.Column(db.String, nullable = False)
    distance =  db.Column(db.Integer, nullable=False)

    def to_dict(self):
        """
        Helper: Returns all database fields as a dict. 
        """
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            distance=self.distance,
        )
