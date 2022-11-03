from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI']="postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development"
    app.config['SQLALCHEMY_TEST_DATABASE_URI']="postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_test"

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.routes import solar_system_bp
    app.register_blueprint(solar_system_bp)

    from app.models.planet import Planet

    return app

    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # if not test_config:
    #     app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    # else:
    #     app.config["TESTING"] = True
    #     app.config['SQLALCHEMY_TEST_DATABASE_URI'] = os.environ.get("SQLALCHEMY_TEST_DATABASE_URI")