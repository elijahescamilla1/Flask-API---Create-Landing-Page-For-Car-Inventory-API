from flask import Blueprint, request, jsonify
from functools import wraps
from .models import Car, db
from .helpers import verify_token

views = Blueprint('views', __name__)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing'}), 403
        try:
            token = token.split()[1]  # Remove 'Bearer' prefix
            current_user = verify_token(token)
            if current_user is None:
                return jsonify({'message': 'Token is invalid'}), 403
        except Exception as e:
            return jsonify({'message': 'Token is invalid', 'error': str(e)}), 403
        return f(current_user, *args, **kwargs)
    return decorated

@views.route('/cars', methods=['POST'])
@token_required
def create_car(current_user):
    data = request.get_json()
    new_car = Car(make=data['make'], model=data['model'], year=data['year'])
    db.session.add(new_car)
    db.session.commit()
    return jsonify({'message': 'Car created successfully'}), 201

@views.route('/cars', methods=['GET'])
@token_required
def get_cars(current_user):
    cars = Car.query.all()
    cars_list = [{'id': car.id, 'make': car.make, 'model': car.model, 'year': car.year} for car in cars]
    return jsonify(cars_list), 200

@views.route('/cars/<int:car_id>', methods=['GET'])
@token_required
def get_car(current_user, car_id):
    car = Car.query.get_or_404(car_id)
    return jsonify({'id': car.id, 'make': car.make, 'model': car.model, 'year': car.year}), 200

@views.route('/cars/<int:car_id>', methods=['PUT'])
@token_required
def update_car(current_user, car_id):
    data = request.get_json()
    car = Car.query.get_or_404(car_id)
    car.make = data['make']
    car.model = data['model']
    car.year = data['year']
    db.session.commit()
    return jsonify({'message': 'Car updated successfully'}), 200

@views.route('/cars/<int:car_id>', methods=['DELETE'])
@token_required
def delete_car(current_user, car_id):
    car = Car.query.get_or_404(car_id)
    db.session.delete(car)
    db.session.commit()
    return jsonify({'message': 'Car deleted successfully'}), 200
