from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request 



bp = Blueprint("planets", __name__, url_prefix="/planet")


def validate_planet(planet_id):
    """
    Helper function to check if planet_id is in 
    database.

    Returns status message to client. 
    """

    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message":f"planet {planet_id} not found"}, 404))

    return planet


@bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    """
    Return a single planet record to the client. 
    Returns JSON.
    Request body ignored. 

    Route: /planet/<planet_id>
    Method: GET
    """

    result_planet = validate_planet(planet_id)
    return result_planet.to_dict()


@bp.route("", methods=["POST"])
def create_planet():
    """
    Add a new planet to the database. 
    Returns status message to the client. 
    Request body must be JSON. 

    Route: /planet/<planet_id>
    Method: POST
    """

    request_body = request.get_json()
    new_planet = Planet(# id=request_body["id"],
                        name=request_body["name"],
                        description=request_body["description"],
                        distance=request_body["distance"])
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@bp.route("", methods=["GET"])
def read_all_planets():
    """
    Send a JSON list of all planets to client
    Returns JSON
    Request body ignored 

    Route: /planet
    Method: GET
    """

    planets = Planet.query.all()
    planets_response = [planet.to_dict() for planet in planets]
    
    return jsonify(planets_response)

@bp.route("/<planet_id>", methods=["PUT"])
def update_a_planet(planet_id):
    """
    Update a planet record in the database. 
    Returns status message to client.
    Request body must be JSON. 

    Route: /planet/<planet_id>
    Method: PUT
    """

    this_p = validate_planet(planet_id)

    request_body = request.get_json()

    this_p.name = request_body["name"]
    this_p.description = request_body["description"]
    this_p.distance = request_body["distance"]

    db.session.commit()
    return make_response(f"Planet '#{this_p.id}', '{this_p.name}' successfully updated")
    
@bp.route("/<planet_id>", methods=["DELETE"])
def delete_a_planet(planet_id):
    """
    Delete a planet from the database.
    Returns status message to client.
    Request body ignored.

    Route: /planet/<planet_id>
    Method: DELETE
    """

    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet '#{planet.id}' '{planet.name}' successfully deleted")

