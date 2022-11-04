import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from models.planet import Planet


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
    Giant_2 = Planet(name ="Giant 2", 
                description="Even bigger than the first!",
                moon_count=130)
    Neptune = Planet(name ="Neptune", 
                description="it may exist, it may not",
                moon_count=0)

    db.session.add_all([Giant_2, Neptune])
    db.session.commit()