from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy() # db and migrate are variables that gives us access to db operations
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #hide a warning abt a feature that we wont be using
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development'
    
    # connects db & migrate to flask app
    db.init_app(app)
    migrate.init_app(app, db)

    from app.models.planet import Planet

    from .routes import planet_bp
    app.register_blueprint(planet_bp)

    return app