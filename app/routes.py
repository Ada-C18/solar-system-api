from flask import Blueprint, jsonify, make_response, abort

planets_bp = Blueprint('planets_bp', __name__, url_prefix='/planets')
