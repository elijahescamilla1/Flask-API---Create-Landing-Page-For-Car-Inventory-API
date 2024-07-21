from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from .models import User

def verify_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        user_id = s.loads(token)['user_id']
    except Exception as e:
        return None
    return User.query.get(user_id)
