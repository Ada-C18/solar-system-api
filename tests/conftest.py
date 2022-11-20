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
    # Arrange
    fake_planet = Planet(name="Big Fake",
                    description="very fake",
                    color="invisible")
    
    db.session.add(fake_planet)
    db.session.commit()

    return fake_planet

@pytest.fixture
def two_saved_planets(app):
    # Arrange
    fake_planet = Planet(name="Big Fake",
                    description="very fake",
                    color="invisible")

    fake_planet2 = Planet(name="Small Fake",
                    description="not as fake",
                    color="polka dots")
    
    db.session.add_all([fake_planet, fake_planet2])
    db.session.commit()
 

