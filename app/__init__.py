from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)

    # dot notation can mean they're in different levels
    from .planets import planets_bp
    app.register_blueprint(planets_bp)

    return app
