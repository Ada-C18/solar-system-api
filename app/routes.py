from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request, abort

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
   
    elif request.method == "GET":
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
        

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response ({"Message": f"Planet {planet_id} invalid."}, 400))
    
    # to access a planet with planet_id in our db, we use
    planet = Planet.query.get(planet_id)
    if not planet:
        abort(make_response({"Message": f"Planet {planet_id} not found."}, 404))
    return planet


@planet_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE"])
def handle_one_planet(planet_id):
    planet = validate_planet(planet_id)
    if request.method == "GET":
        return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "moons": planet.moons    
        }

    elif request.method == "PUT":
        request_body = request.get_json()

    #updating the attributes
        planet.name = request_body["name"]
        planet.description = request_body["description"]
        planet.moons = request_body["moons"]

    # commit changes to our db
        db.session.commit()

        return make_response(f"Planet #{planet_id} is updated.")

    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()

        return make_response(f"Planet #{planet_id} is deleted.")


