from flask import Blueprint,jsonify,abort,make_response,request
from app import db
from app.models.planet import Planet


if title_query:
        title_query = title_query.filter_by(title=title_query)


planets_bp = Blueprint('planets_bp', __name__, url_prefix='/planets')

@planets_bp.route('', methods=['GET'])
def handle_planet():
    planet_query = Planet.query


    description_query = request.args.get("description")
    
    if description_query:
        planet_query = planet_query.filter_by(description=description_query)
    else:
        planets = Planet.query.all()

    color_query = request.args.get("color")
    if color_query:
        planet_query = planet_query.filter_by(color=color_query)
    else:
        planets = Planet.query.all()

    name_query = request.args.get("name")
    if name_query:
        planet_query = planet_query.filter_by(name=name_query)
        
    planets = planet_query.all()

        
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "color": planet.color,
            "description": planet.description
        })

        if not planets_response:
            return make_response(jsonify(f"There are no {planet_query} planets"))
        return jsonify(planets_response)

    board_response = []
    for board in boards:
        board_response.append({
            "id": planet.id,
            "name": planet.name,
            "color": planet.color,
            "description": planet.description
        })

        if not planets_response:
            return make_response(jsonify(f"There are no {planet_query} planets"))
        return jsonify(planets_response)


@planets_bp.route("/<id>", methods=['GET','PUT','DELETE'])

def handle_1_planet(id):
    planet = Planet.query.get(id)

    
    if request.method == "GET":
        return{
            "id": planet.id,
            "name": planet.name,
            "color": planet.color,
            "description": planet.description
        }
    elif request.method == "PUT":
        request_body = request.get_json()
        
        planet.name = request_body["name"]
        planet.color = request_body["color"]
        planet.description = request_body["description"]

        
        db.session.commit()
        return make_response(f"planet color {planet.color} succesfully updated",200)

    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()

        return make_response(f"planet color {planet.color} succesfully deleted", 200)

            

@board_bp.route(/title, methods=["GET"])
# GET /task/id
def handle_task(title):
    # Query our db to grab the task that has the id we want:
    
    task = Task.query.get(title)

    if task.goal_id is not None:
        return{"task": task.to_dict_in_goal()}
    else:
        return {"task": task.to_dict()}

