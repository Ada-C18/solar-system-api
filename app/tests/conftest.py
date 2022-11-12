import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.planet import Planet

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(send, response, **extra):
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
def one_planet(app):
    # Arrange
    ocean_planet = Planet(name="Mercury", description="watr 4evr",
                        diameter="39999")
    

    db.session.add(ocean_planet)
    # Alternatively, we could do
    # db.session.add(ocean_planet)
    # db.session.add(mountain_book)
    db.session.commit()
    return ocean_planet