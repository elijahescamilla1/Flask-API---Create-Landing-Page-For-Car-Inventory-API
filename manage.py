from flask_script import Manager
from flask_migrate import MigrateCommand
from create_app import create_app, db

app = create_app()
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
