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
    planet_mercury = Planet(name="Mercury",
                      description="The smallest planet",
                      radius = 1516)
    planet_venus = Planet(name="Venus",
                         description="The second planet from the Sun and Earth's closest planetary neighbor",
                         radius = 3760)

    db.session.add_all([planet_mercury, planet_venus])
    db.session.commit()
