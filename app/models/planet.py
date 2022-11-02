from app import db


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    color = db.Column(db.String)

    def to_dict(self):
        return dict(
            id = self.id,
            name = self.name,
            description = self.description,
            color = self.color)

    @classmethod
    def from_dict(cls, data_dict):
        return Planet(name = data_dict["name"],
                    color = data_dict["color"],
                    description = data_dict["description"])


# planets = [
#     Planet(1,"Earth","big","blue/green"),
#     Planet(2,"Mars","smaller","red"),
#     Planet(3,"Venus","a little bigger","gold")]