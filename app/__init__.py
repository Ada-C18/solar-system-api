from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)
    
    # Where I am listening for my database
    # Ignore a warning
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    # Connects Flask to the Database
    # Tells FLask where to find our database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development'


    # Connects db to migrate to our FLask app
    db.init_app(app)
    migrate.init_app(app, db)

    # Add import for Planet
    from app.models.planet_model import Planet

    from app.routes import planets_bp
    app.register_blueprint(planets_bp)    
    

    return app
