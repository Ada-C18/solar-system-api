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
    # Arrange
    ocean_planet = Planet(name="Ocean Planet",
                    description="watr 4evr",
                    diameter = "0 miles")
    mountain_planet = Planet(name="Mountain Planet",
                        description="i luv 2 climb rocks",
                        diameter = "1 mile")

    db.session.add_all([ocean_planet, mountain_planet])
    db.session.commit()