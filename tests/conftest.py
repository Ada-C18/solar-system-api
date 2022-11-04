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
def one_saved_planet(app):
    planet = Planet(name="Adie", 
            distance_from_sun=10, 
            description="determined and possibly girlbossing too close to the sun")
    db.session.add(planet)
    db.session.commit()
    return planet