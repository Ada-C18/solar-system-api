from app import db
from flask import abort, make_response


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    diameter = db.Column(db.Integer)
    

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "diameter": self.diameter,
            "id": self.id
    }

    @classmethod
    def from_dict(cls,req_body):
        return cls(
        name=req_body['name'], 
        description=req_body['description'], 
        diameter=req_body['diameter']
    )

    def update(self,req_body):
        # try:
        self.name = req_body["name"]
        self.description = req_body["description"]
        self.diameter = req_body["diameter"]
        # except KeyError as error:
        #     abort(make_response({'message': f"Missing attribute: {error}"}))