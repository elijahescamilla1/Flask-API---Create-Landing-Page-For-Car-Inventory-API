import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from car_collection_api import create_app, db
from car_collection_api.auth.models import User

app = create_app()
app.app_context().push()

user = User(email='admin@example.com', password='adminpassword')
db.session.add(user)
db.session.commit()

print('Admin user created successfully!')
