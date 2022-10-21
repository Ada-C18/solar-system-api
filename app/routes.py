
from flask import Blueprint , jsonify

solar_system_bp = Blueprint("solar_system", __name__)

class Planet:
    def __init__(self , id , name, description, size):
        self.id = id
        self.name=name
        self.description = description
        self.size=size
planets = [
    Planet(1, "Fictional Book Title", "A fantasy novel set in an imaginary world.", 2),
    Planet(2, "Fictional Book Title", "A fantasy novel set in an imaginary world.", 3),
    Planet(3, "Fictional Book Title", "A fantasy novel set in an imaginary world.", 4)
]
solar_system_bp=Blueprint("planets",__name__ ,  url_prefix="/planets") 
@solar_system_bp.route("",methods=["GET"])  
def handle_planet():
    result=[]
    for i in planets:
        result.append({
            "id":i.id,
            "name":i.name,  
            "description":i.description,
            "size":i.size
        })  
    return jsonify(result) 

