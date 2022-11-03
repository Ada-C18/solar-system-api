from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request 



bp = Blueprint("planets", __name__, url_prefix="/planet")


def validate_object_by_id(cls, model_id):
    """
    Helper function to check if a record is is in 
    database using the model class and model id. 

    Returns status message to client if passed id isn't int or 
    id not in database.

    Returns database model object to calling function if record is found. 
    """

    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"{cls.__name__} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)

    if not model:
        abort(make_response({"message":f"{cls.__name__} {model_id} not found"}, 404))

    return model


@bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    """
    Return a single planet record to the client. 
    Returns JSON.
    Request body ignored. 

    Route: /planet/<planet_id>
    Method: GET
    """

    result_planet = validate_object_by_id(Planet,planet_id)
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
    new_planet = Planet.from_dict(request_body)
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

    # create a list of columns to search by 
    columns = ["id", "name", "description", "distance"]

    # filter request.arg for valid column names
    # query_dict = {k:v for (k,v) in request.args.items() if k in columns}
    query_dict = {}
    for key in columns:
        value = request.args.get(key)
        if value:
            query_dict[key] = value

    planet_query = Planet.query

    planet_query = planet_query.filter_by(**query_dict)
    
    planets = planet_query.all()

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

    this_p = validate_object_by_id(Planet,planet_id)

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

    planet = validate_object_by_id(Planet, planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet '#{planet.id}' '{planet.name}' successfully deleted")

