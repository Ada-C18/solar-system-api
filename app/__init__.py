from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)
    
    from .routes import  solar_system_bp
    app.register_blueprint(solar_system_bp)
    

    return app
