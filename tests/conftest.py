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
    planet = Planet(name="Pluto", description="cold and icy", distance=15)
    db.session.add(planet)
    db.session.commit()
    return planet

@pytest.fixture
def two_saved_planets(app):
    planet1 = Planet(name="Pluto", description="cold and icy", distance=15)
    planet2 = Planet(name="Venus", description="round and far away", distance= 42)
    db.session.add_all([planet1, planet2])