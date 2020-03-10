""" Script to Manage Kambium Databases
"""
from os import environ
from flask import current_app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import database_manager, db

app = database_manager()

#* Models need to be imported after db initialised.
from app.backend.api.resource.user import model

from app.backend.auth import model

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':

    with app.app_context():
        manager.run()

