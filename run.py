import sys
print("Python Path:", sys.path)

from car_collection_api.app import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
