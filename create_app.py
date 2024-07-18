from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres.bedlmcmwyjtgsnahdarh:[Lifetime__20xqw]@aws-0-us-west-1.pooler.supabase.com:6543/postgres'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    login_manager.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    print("Initialized Extensions")

    from car_collection_api.auth.routes import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from car_collection_api.main.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

if __name__ == "__main__":
    app = create_app()
    print("App Created")
    app.run(debug=True)
