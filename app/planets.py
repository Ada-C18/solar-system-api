

# @planets_bp.route('/<planet_id>', methods=['GET'])
# def get_one_planet(planet_id):
#     pass

# def validate_planet(id):
#     try:
#         planet_id = int(id)
#     except ValueError:
#         return {
#             "message": "Invalid planed id"
#         }, 400

#     for planet in PLANETS:
#         if planet.id == planet_id:
#             return vars(planet)

#     abort(make_response(jsonify(description="Resource not found"), 404))