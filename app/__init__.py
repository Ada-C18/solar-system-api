from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


def create_app(test_config=None):
    app = Flask(__name__)

    from.routes import planets_bp
    app.register_blueprint(planets_bp)

    return app
