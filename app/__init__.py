from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


def create_app(test_config=None):
    app = Flask(__name__)

    db = SQLAlchemy()
    migrate = Migrate()

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development'

    from .routes import planets_bp
    app.register_blueprint(planets_bp)

    db.init_app(app)
    migrate,init_app(app, db)

    from app.models.planet_model import Planet

    return app