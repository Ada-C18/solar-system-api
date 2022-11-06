from flask import Blueprint, jsonify, make_response, abort

planets_bp = Blueprint('planets_bp', __name__, url_prefix='/planets')


'''
WAVE 3!!
Need to create endpoints with following functionality:
    - 'POST' request to create new valid planet
        * should receive a a success response
    - 'GET' request to get all existing planets
        * list should include
            - planet id
            - planet name
            - planet description
'''