from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)


'''
Planet descriptions for Postman POST HTML requests bodies:
{
    "name": "Mercury",
    "description": "The smallest planet in our solar system and closest to the Sun. It is only slightly larger than Earth's Moon."
}
{
    "name": "Venus",
    "description": "Spins slowly in the opposite direction from most planets. A thick atmosphere traps heat in a runaway greenhouse effect."
}

{
    "name": "Earth",
    "description": "The only place that's inhabited by living things. Also, the only planet in our solar system with liquid water on the surface."
}

{
    "name": "Mars",
    "description": "A dusty, cold desert world with a very thin atmosphere."
}
{
    "name": "Jupiter",
    "description": "More than twice as massive than other planets in our solar system combined."
}
{
    "name": "Saturn",
    "description": "Adorned with a dazzling, complex system of icy rings."
}
{
    "name": "Uranus",
    "description": "Rotates at a nearly 90-degree angle from the plane of its orbit."
}
{
    "name": "Neptune",
    "description": "Is dark, cold and whipped by supersonic winds. First planet located through mathematical calculations."
}
'''