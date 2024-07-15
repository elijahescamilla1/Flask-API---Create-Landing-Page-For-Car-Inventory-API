from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    token = db.Column(db.String(32), index=True, unique=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_token(self, expires_in=600):
        now = int(time())
        if self.token and self.token_expiration > now + 60:
            return self.token
        self.token = jwt.encode(
            {'get_token': self.id, 'exp': now + expires_in},
            current_app.config['SECRET_KEY'], algorithm='HS256')
        self.token_expiration = now + expires_in
        db.session.add(self)
        return self.token
