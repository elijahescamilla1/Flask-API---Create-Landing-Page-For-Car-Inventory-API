import sys
import os
from werkzeug.security import generate_password_hash

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from car_collection_api import create_app, db
from car_collection_api.models import User

app = create_app()
app.app_context().push()

user = User(email='john.doe@example.com', password=generate_password_hash('password'))
db.session.add(user)
db.session.commit()

print('User created successfully!')
