from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)

    # register Blueprints here
    from .routes import planet_bp
    app.register_blueprint(planet_bp)

    return app
