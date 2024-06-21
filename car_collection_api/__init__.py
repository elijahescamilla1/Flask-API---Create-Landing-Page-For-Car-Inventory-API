from flask import Flask
from .auth.routes import auth_bp
from .cars.routes import cars_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('car_collection_api.config.Config')

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(cars_bp)

    return app
