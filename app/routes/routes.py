from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, abort, request

bp = Blueprint("planets", __name__, url_prefix="/planets")

# Helper function
def  validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message": f"{cls.__name__} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)
    if not model:
        abort(make_response({"message": f"{cls.__name__} {model_id} not found"}, 404))
    
    return model


@bp.route("", methods=["GET"])
def get_all_planets():
    size_query = request.args.get("size")

    planet_query = Planet.query # returns an instance of base query

    if size_query:
        planet_query = planet_query.filter_by(size=size_query) #returns a new query - another instance of a base query
   
    planets = planet_query.all() # returns a list of planet instances
    
    planets_response = [planet.to_dict() for planet in planets]
    return jsonify(planets_response), 200


@bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    return jsonify(planet.to_dict()), 200 

@bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    request_body = request.get_json()
    planet.name=request_body["name"],
    planet.size=request_body["size"],
    planet.description=request_body["description"]

    db.session.commit()
    return make_response(f"Planet {planet.name} was successfully updated", 200)
        
@bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet {planet.name} was successfully deleted", 200)
      


@bp.route("", methods = ["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)

    db.session.add(new_planet)
    db.session.commit()
    return make_response(f"Planet {new_planet.name} was successfully created", 201)






