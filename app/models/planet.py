from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    flag = db.Column(db.Boolean)

    @classmethod
    def from_dict(cls,input_data):
        return cls(
                    name=input_data["name"],
                    description=input_data["description"],
                    flag=input_data["flag"]
                )

    def to_dict(self):
        return dict(
                    id=self.id,
                    name=self.name,
                    description=self.description,
                    flag=self.flag
                )