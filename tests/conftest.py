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
    kangaroo_planet = Planet(name="Kangaroo Planet",
    description="Australia wasn't big enough for them",
    color="Brown and Gray")

    db.session.add(kangaroo_planet)
    db.session.commit()

@pytest.fixture
def two_saved_planets(app):
    cat_planet = Planet(name="Cat Planet",
    description="Funny",
    color="Gray")
    dog_planet = Planet(name="Dog Planet",
    description="Big",
    color="Brown")

    db.session.add_all([cat_planet, dog_planet])
    db.session.commit()