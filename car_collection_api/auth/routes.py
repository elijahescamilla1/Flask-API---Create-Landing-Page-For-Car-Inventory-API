from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, login_required
from car_collection_api import db, login_manager
from car_collection_api.auth.models import User
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and check_password_hash(user.password, data['password']):
        login_user(user)
        return jsonify({'message': 'Logged in successfully'}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully'}), 200
