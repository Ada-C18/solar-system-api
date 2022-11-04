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
def two_saved_planets(app):

    mercury = Planet(
        name="Mercury",
        description="distance_from_sun: 36.04 million mi",
        num_moons=0)

    venus = Planet(
        name="Venus",
        description="distance_from_sun: 67.24 million mi",
        num_moons=0)

    db.session.add_all([mercury, venus])
    db.session.commit()