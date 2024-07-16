from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/signup')
def signup():
    return "Signup Page"
