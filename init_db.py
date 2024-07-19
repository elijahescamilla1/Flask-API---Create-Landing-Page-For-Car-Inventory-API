from car_collection_api import create_app, db
from car_collection_api.models import User, Car
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()
    
    # Create a test user
    if not User.query.filter_by(email='test@example.com').first():
        test_user = User(email='test@example.com', password=generate_password_hash('password'))
        db.session.add(test_user)
    
    # Create sample cars
    if not Car.query.all():
        car1 = Car(make='Toyota', model='Corolla', year=2020)
        car2 = Car(make='Honda', model='Civic', year=2019)
        db.session.add(car1)
        db.session.add(car2)
    
    db.session.commit()
