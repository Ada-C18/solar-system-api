from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import dotenv_values
import os


db = SQLAlchemy() # db and migrate are variables that gives us access to db operations
migrate = Migrate()
config = dotenv_values(".env")


print(config["SQLALCHEMY_DATABASE_URI"])

def create_app(test_config=None):
    app = Flask(__name__)
    if not test_config:
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #hide a warning abt a feature that we wont be using
        app.config['SQLALCHEMY_DATABASE_URI'] = config["SQLALCHEMY_DATABASE_URI"]
    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = config["SQLALCHEMY_TEST_DATABASE_URI"]

    # connects db & migrate to flask app
    from app.models.planet import Planet

    db.init_app(app)
    migrate.init_app(app, db)


    from .routes import planet_bp
    app.register_blueprint(planet_bp)

    return app