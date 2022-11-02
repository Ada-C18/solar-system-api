from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet


# class Planet:
#     def __init__(self,id,name,description,color):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.color = color

#     def to_json(self):
#         return dict(
#             id= self.id,
#             name = self.name,
#             description = self.description,
#             color = self.color)


# planets = [
#     Planet(1,"Earth","big","blue/green"),
#     Planet(2,"Mars","smaller","red"),
#     Planet(3,"Venus","a little bigger","gold")


# @bp.route("", methods=["GET"])
# def handle_planets():
#     all_planets = []
#     for planet in planets:
#         all_planets.append(planet.to_json())
#     return jsonify(all_planets)

# def validate_planet(planet_id):
#     try:
#       planet_id = int(planet_id)
#     except:
#       abort(make_response({"message":f"planet {planet_id} invalid"}, 400))
    
#     for planet in planets:
#         if planet.id == planet_id:
#             return planet

#     abort(make_response({"message":f"planet {planet_id} not found"}, 404))
    


# @bp.route("/<planet_id>", methods=["GET"])
# def handle_planet(planet_id):
#     planet = validate_planet(planet_id)
#     return (planet.to_json())

    
bp = Blueprint("planets", __name__, url_prefix="/planets")

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message": f"{cls.__name__} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)

    if not model:
        abort(make_response({"message": f"{cls.__name__} {model_id} not found"}, 404))

    return model

@bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@bp.route("", methods=["GET"])
def read_all_planet():
    name_query = request.args.get("name")
    color_query = request.args.get("color")
    description_query = request.args.get("description")
    id_query = request.args.get("id")

    planet_query = Planet.query

    if name_query:
        planet_query = planet_query.filter_by(name=name_query) 

    if color_query:
        planet_query = planet_query.filter_by(color=color_query)

    if description_query:
        planet_query = planet_query.filter_by(description = description_query)

    if id_query:
        planet_query = planet_query.filter_by(id= id_query)
   
    planets = planet_query.all()
    
    all_planets = [planet.to_dict() for planet in planets]

    return jsonify(all_planets), 200

@bp.route("/<id>", methods=["GET"])
def read_one_planet(id):
    planet = validate_model(Planet, id)
    return jsonify(planet.to_dict()), 200

@bp.route("/<id>", methods=["PUT"])
def update_planet(id):
    planet = validate_model(Planet, id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.color = request_body["color"]
    planet.description = request_body["description"]

    db.session.commit()

    return make_response(f"planet #{id} successfully updated"), 200

@bp.route("/<id>", methods=["DELETE"])
def delete_plante(id):
    planet = validate_model(Planet, id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"planet #{id} successfully deleted"), 200 


