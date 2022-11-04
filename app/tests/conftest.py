import pytest
from app import create_app
from app import db
from app.models.planet import Planet
from flask.signals import request_finished

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
def saved_test_planets(app):

    test_planet1 = Planet(color= "pink", is_dwarf= True, livability= 3, moons= 99, name= "Pretend Planet X")
    test_planet2 = Planet(color= "purple", is_dwarf= False, livability= 7.4, moons= 1, name= "Planet Pretend Z")

    db.session.add_all([test_planet1, test_planet2])
    db.session.commit()

    # return [test_planet1, test_planet2]