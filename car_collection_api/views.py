from flask import Blueprint, request, jsonify
from flask_login import login_required
from .models import Car, db

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return "Welcome to the Car Collection API"

@views.route('/test', methods=['GET'])
def test():
    return "Test route is working!"

@views.route('/cars', methods=['POST'])
@login_required
def create_car():
    data = request.get_json()
    new_car = Car(make=data['make'], model=data['model'], year=data['year'])
    db.session.add(new_car)
    db.session.commit()
    return jsonify({'message': 'Car created'}), 201

@views.route('/cars', methods=['GET'])
def get_cars():
    cars = Car.query.all()
    return jsonify([car.to_dict() for car in cars]), 200

@views.route('/cars/<int:id>', methods=['GET'])
def get_car(id):
    car = Car.query.get_or_404(id)
    return jsonify(car.to_dict()), 200

@views.route('/cars/<int:id>', methods=['PUT'])
@login_required
def update_car(id):
    data = request.get_json()
    car = Car.query.get_or_404(id)
    car.make = data['make']
    car.model = data['model']
    car.year = data['year']
    db.session.commit()
    return jsonify({'message': 'Car updated'}), 200

@views.route('/cars/<int:id>', methods=['DELETE'])
@login_required
def delete_car(id):
    car = Car.query.get_or_404(id)
    db.session.delete(car)
    db.session.commit()
    return jsonify({'message': 'Car deleted'}), 200
