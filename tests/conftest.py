import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.planet import Planet

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def one_planet(app):
    planet = Planet(name="venus", 
                    description="doesn't have any moons, 2nd largest planet.", 
                    flag=False)

    db.session.add(planet)
    db.session.commit()
    return planet

@pytest.fixture
def multi_planets(app):
    planet_one = Planet(name="venus", 
                        description="doesn't have any moons, 2nd largest planet.", 
                        flag=False)
    planet_two = Planet(name="Neptune", 
                        description="one of two ice giant planets.", 
                        flag=False)
                        
    planet_list = [planet_one, planet_two]

    db.session.add_all(planet_list)
    db.session.commit()
