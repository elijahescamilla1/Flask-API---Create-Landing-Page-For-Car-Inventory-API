from flask import Flask
from .models import db, User, Car
from flask_login import LoginManager
from .auth import auth as auth_blueprint
from .views import views as views_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.register_blueprint(auth_blueprint, url_prefix='/')
    app.register_blueprint(views_blueprint, url_prefix='/')

    with app.app_context():
        db.create_all()

    return app
