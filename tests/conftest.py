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

# planets = [
#     Planet(1, "Mercury", "solid", 0),
#     Planet(2, "Venus", "bright and volcanic", 0),
#     Planet(3, "Earth", "half and half", 1)
# ]

@pytest.fixture
def two_saved_planets(app):
    mercury = Planet(name="Mercury", description="solid", moons=0)
    venus = Planet(name="Venus", description="bright and volcanic", moons=0)

    db.session.add_all([mercury, venus])
    db.session.commit()