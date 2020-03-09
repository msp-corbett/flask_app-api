""" Flask Migrate script """
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import database_manager

if __name__ == '__main__':
    app.run()