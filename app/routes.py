from flask import Blueprint, jsonify
from sqlalchemy import desc
from .planets import *
planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

@planet_bp.route("", methods = ["GET"])
def read_planets():
    return return_all_planets()

@planet_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    return verify_planet(planet_id)    
            
    
        
