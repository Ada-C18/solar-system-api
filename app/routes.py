from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet

planet_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planet_bp.route("", methods=["GET", "POST"])
def handle_planets():
    if request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(name=request_body["name"], 
                            description=request_body["description"],
                            flag=request_body["flag"])
        db.session.add(new_planet)
        db.session.commit()
        return make_response(f"planet {new_planet.name} successfully created!", 201)
    
    elif request.method == "GET":
        planets = Planet.query.all()
        planets_response = [planet.to_dict() for planet in planets]
        return jsonify(planets_response)

# Would we add a query param here? ^ 

@planet_bp.route("/<id>", methods=["GET"])
def get_planet(id):
    validate_model(Planet, id)
    planet = Planet.query.get(id)
    return jsonify(planet.to_dict())

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message": f"object '{model_id}' is invalid"}, 400))
    
    model = cls.query.get(model_id)
    if not model:
        abort(make_response({"message": f"{model_id} not found"}, 404))