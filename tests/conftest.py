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
def two_saved_planets(app):
    big_planet = Planet(name="Jupiter",
    description="big planet", moons = 80)
    small_planet =  Planet(name="Mercury",
    description="small planet", moons=0)

    db.session.add_all([big_planet, small_planet])
    db.session.commit()