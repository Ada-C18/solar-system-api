from time import monotonic_ns
from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request

planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

@planet_bp.route("", methods=["POST", "GET"])
def handle_planets():
    if request.method == "POST":
        request_body = request.get_json()
        planet_1 = Planet(
            name = request_body["name"], 
            description = request_body["description"],
            moons = request_body["moons"])
        db.session.add(planet_1)
        db.session.commit()

        return make_response(f"Planet {planet_1.name} successfully created", 201)
    
    if request.method == "GET":
        response_body = []
        planets= Planet.query.all()
        for planet in planets:
            response_body.append({
                "name": planet.name,
                "description": planet.description,
                "moons": planet.moons,
                "id": planet.id,
            })
            
        return jsonify(response_body), 200