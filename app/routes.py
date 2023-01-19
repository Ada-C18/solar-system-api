from crypt import methods
from app import db
from app.models.planet_model import Planet
from flask import Blueprint, jsonify, abort, make_response, request

planets_bp = Blueprint('planets_bp', __name__, url_prefix='/planets')

@planets_bp.route('', methods=["GET", "POST"])
def handle_planets():     
    planet = Planet.query.all()
    if request.method == "GET":
        if not planet:
            return make_response("Non-existing planet", 404)
        else:
            planet_response = []
            for planet in planets:
                planet_response.append({
                    "id": planet.id,
                    "name": planet.name,
                    "description": planet.description,
                    "rings": planet.rings
                })
            return jsonify(planet_response), 200
    
    elif request.method == "POST":
        request_body = request.get_json()
        if "name" not in request_body or "description" not in request_body:
            return make_response("Invalid Request, Name & Description Can't Be Empty", 400)

        new_planet = Planet(
        # You're looking for this key and assign it to name, breed, gender, age
        name=request_body["name"],
        description=request_body["description"],
        rings=request_body["rings"],
    )
        
        db.session.add(new_planet)
        db.session.commit()

        # Successful response
        return make_response(f"Planet {new_planet.name} has been successfully created!", 201)
        
# GET ONE PLANET
@planets_bp.route('/<id>', methods=["GET", "PUT", "DELETE"])
def handle_planet(id):
    planet = Planet.query.get(planet_id)
    
    if request.method == "GET":
        if not planet:
            return make_response("Non-existing planet", 404)
        # Send back a single JSON object (dictionary):
        else:
            return {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "rings": planet.rings
            }
        
    elif request.method == "PUT":
        request_body = request.get_json()
        
        planet.name = request_body["name"],
        planet.description = request_body["description"],
        planet.rings = request_body["rings"]
        
        db.session.commit()
        return make_response(f"Planet {planet.name} successfully updated", 200)
    
    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()
        
        return make_response(f"Planet {planet.name} successfully deleted", 202)