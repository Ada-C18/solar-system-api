from flask import Blueprint, jsonify
from sqlalchemy import desc
from .planets import *
planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

@planet_bp.route("", methods = ["GET"])
def read_planets():
    return return_all_planets()

@planet_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        return {"Message": f"Planet {planet_id} invalid."}, 400

    for planet in list_of_planets:
        if planet.id == planet_id:
            return {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description
            }
    return {"Message": f"Planet {planet_id} not found."}, 404
        
