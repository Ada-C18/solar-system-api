from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    size = db.Column(db.Integer, nullable=False)

    @classmethod
    def from_dict(cls, data_dict):
      return cls(
        name=data_dict["name"],
        size=data_dict["size"],
        description=data_dict["description"]
        )

    def to_dict(self):
          return dict(
            id=self.id, 
            name=self.name, 
            description=self.description,
            size=self.size)