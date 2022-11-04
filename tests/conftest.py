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
    # arrange
    Saturn = Planet(
        id=1,
        name="Saturn",
        surface_area=123890491,
        moons=83,
        distance_from_sun=123123123123,
        namesake="The Roman god of time"
    )
    Mars = Planet(
        id=2,
        name="Mars",
        surface_area=1010101,
        moons=1,
        distance_from_sun=123123123123,
        namesake="The Roman god of time"
    )

    db.session.add_all([Saturn, Mars])
    db.session.commit()
