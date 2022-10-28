from flask import Blueprint, jsonify, abort, make_response, request
from app.models.planet import Planet
from app import db

planets_bp = Blueprint("planets_bp", __name__, url_prefix = "/planets")

# CREATE RESOURCE
@planets_bp.route("", methods = ["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name = request_body['name'],
        color = request_body['color'],
        description = request_body['description'] 
        )
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} has been created", 201)


# GET ALL RESOURCES
@planets_bp.route("", methods = ["GET"])
def get_all_planets():
    results_list = []
    all_planets = Planet.query.all()

    for planet in all_planets:
        results_list.append(
            {"id": planet.id,
            "name": planet.name,
            "color": planet.color,
            "description": planet.description
        })

    return jsonify(results_list), 200



# # class Planet:
# #     def __init__(self, id, name, color, description):
# #         self.id = id
# #         self.name = name
# #         self.color = color
# #         self.description = description

# # planets = [
# #     Planet(1, "Saturn", "yellowish-brown", "Saturn is the sixth planet from the Sun and the second-largest planet in our solar system."),
# #     Planet(2, "Mars", "rusty red", "Mars is the fourth planet from the Sun – a dusty, cold, desert world with a very thin atmosphere."),
# #     Planet(3, "Jupiter", "beige", "Jupiter is covered in swirling cloud stripes. It has big storms like the Great Red Spot, which has been going for hundreds of years. "),
# #     Planet(4, "Earth", "blue and green", "Earth is a rocky, terrestrial planet. It has a solid and active surface with mountains, valleys, canyons, plains and so much more."),
# #     Planet(5, "Venus", "beige", "It’s one of the four inner, terrestrial (or rocky) planets, and it’s often called Earth’s twin because it’s similar in size and density."),
# #     Planet(6, "Uranus", "blue", "Uranus is the seventh planet from the Sun, and has the third-largest diameter in our solar system."),
# #     Planet(7, "Neptune", "blue", "Dark, cold, and whipped by supersonic winds, ice giant Neptune is the eighth and most distant planet in our solar system"),
# #     Planet(8, "Pluto", "off-white and light blue", "Pluto is a dwarf planet in the Kuiper Belt, a donut-shaped region of icy bodies beyond the orbit of Neptune."),
# #     Planet(9, "Mercury", "dark gray", "Mercury—the smallest planet in our solar system and closest to the Sun—is only slightly larger than Earth's Moon.")


# # ]

# # planets_bp = Blueprint("planets_bp", __name__, url_prefix = "/planets")

# # @planets_bp.route("", methods = ["GET"])
# # def get_all_planets():
# #     planets_response = []
# #     for planet in planets:
# #         planets_response.append(
# #         {"id": planet.id,
# #             "name": planet.name,
# #             "color": planet.color,
# #             "description": planet.description
#         }
#         )
#     return jsonify(planets_response)


# def validate_planet_id(id):
#     try:
#         planet_id = int(id)
#     except:
#         abort(make_response({"message":f"Planet {id} is invalid"}, 400))
    
#     for planet in planets:
#         if planet.id == planet_id:
#             return planet
        
#     abort(make_response({"message":f"Planet {id} is not found"}, 404))

# @planets_bp.route("/<id>", methods = ["GET"])
# def get_one_planet(id):
    # try:
    #     planet_id = int(id)
    # except:
    #     abort(make_response({"message":f"Planet {id} is invalid"}, 400))
    
    # planet = int(id)
    # for planet in planets:
    #     if planet.id == planet_id:
    # planet = validate_planet_id(id)
    # return (
    #     {"id": planet.id,
    #         "name": planet.name,
    #         "color": planet.color,
    #         "description": planet.description
    #     }
    # )
        
