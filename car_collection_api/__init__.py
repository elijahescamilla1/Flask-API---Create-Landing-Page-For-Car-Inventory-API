from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)
    ma.init_app(app)

    from car_collection_api.auth.routes import auth
    from car_collection_api.main.routes import main
    app.register_blueprint(auth)
    app.register_blueprint(main)

    return app