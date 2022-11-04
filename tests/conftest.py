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


# @pytest.fixture
# def two_saved_books(app):
# # Arrange
# ocean_book = Book(title="Ocean Book",
#                     description="watr 4evr")
# mountain_book = Book(title="Mountain Book",
#                         description="i luv 2 climb rocks")

# db.session.add_all([ocean_book, mountain_book])
# # Alternatively, we could do
# # db.session.add(ocean_book)
# # db.session.add(mountain_book)
# db.session.commit()