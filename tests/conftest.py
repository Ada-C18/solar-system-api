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

# This fixture gets called in every test that
# references "one_task"
# This fixture creates a task and saves it in the database
@pytest.fixture
def one_planet(app):
    new_planet = Planet(
        name="Planet_Test", description="Very testy", color="green", id=1)
    db.session.add(new_planet)
    db.session.commit()


@pytest.fixture
def two_saved_planets(app):
# Arrange
    planet1 = Planet(
        name="Planet_Test", description="Very testy", color="green", id=1)
    planet2 = Planet(
        name="Planet_Test_2", description="Very testy 2", color="green 2", id=2)

    db.session.add_all([planet1, planet2])
    db.session.commit()