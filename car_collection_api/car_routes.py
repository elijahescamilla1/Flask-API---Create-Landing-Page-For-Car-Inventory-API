from flask import Blueprint, request, jsonify
from flask_login import login_required
from app.models import Car  # Importing the Car model from models.py
from app import db  # Importing db from __init__.py

car_bp = Blueprint('car', __name__)

@car_bp.route('/cars', methods=['POST'])
@login_required
def create_car():
    data = request.get_json()
    new_car = Car(make=data['make'], model=data['model'], year=data['year'])
    db.session.add(new_car)
    db.session.commit()
    return jsonify({'message': 'Car created successfully'}), 201

@car_bp.route('/cars', methods=['GET'])
@login_required
def get_cars():
    cars = Car.query.all()
    cars_list = [{'id': car.id, 'make': car.make, 'model': car.model, 'year': car.year} for car in cars]
    return jsonify(cars_list), 200

@car_bp.route('/cars/<int:car_id>', methods=['GET'])
@login_required
def get_car(car_id):
    car = Car.query.get_or_404(car_id)
    return jsonify({'id': car.id, 'make': car.make, 'model': car.model, 'year': car.year}), 200

@car_bp.route('/cars/<int:car_id>', methods=['PUT'])
@login_required
def update_car(car_id):
    data = request.get_json()
    car = Car.query.get_or_404(car_id)
    car.make = data['make']
    car.model = data['model']
    car.year = data['year']
    db.session.commit()
    return jsonify({'message': 'Car updated successfully'}), 200

@car_bp.route('/cars/<int:car_id>', methods=['DELETE'])
@login_required
def delete_car(car_id):
    car = Car.query.get_or_404(car_id)
    db.session.delete(car)
    db.session.commit()
    return jsonify({'message': 'Car deleted successfully'}), 200
