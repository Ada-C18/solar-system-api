import pytest
from app import create_app, db
from app.models.planet import Planet
from flask.signals import request_finished

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(send, response, **extra):
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
    planet = Planet(
        name = "Uranus",
        color = "blue",
        description = "Uranus is the seventh planet from the Sun, and has the third-largest diameter in our solar system."
    )
    db.session.add(planet)
    db.session.commit()
    db.session.refresh(planet, ["id"])
    return planet