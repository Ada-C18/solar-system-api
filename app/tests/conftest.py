import pytest
from app import create_app, db
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
def two_saved_planets(app):
    # Arrange
    venus_planet = Planet(name="Venus", description="Hot mama", mass="The bigger the better.")
    earth_planet = Planet(name="Earth", description="There are bugs here", mass="normal")

    db.session.add_all([venus_planet, earth_planet])
    db.session.commit()
