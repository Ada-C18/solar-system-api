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
    first_planet = Planet(name="Mercury", description="Covered with craters", miles_from_sun="40 million")
    second_planet = Planet(name="Venus", description="Considered Earth's twin", miles_from_sun="67 million")
    
    db.session.add_all([first_planet, second_planet])
    db.session.commit()

