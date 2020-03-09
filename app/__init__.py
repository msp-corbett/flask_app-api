""" A Flask App + API Example"""
from os import environ
from flask import (
    Flask, jsonify, session)
from flask.wrappers import Response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from flask_principal import (
    Principal, Identity, identity_changed,
    current_app)
from flask_restful import Api
from flask_marshmallow import Marshmallow
from app.reverse_proxy import ReverseProxied

from app.backend.api.resource.user.model import User

db = SQLAlchemy()
ma = Marshmallow()
api = Api()
migrate = Migrate()
manager = Manager()
csrf = CSRFProtect()
principals = Principal()

login = LoginManager()
login.login_view = 'auth_route.login'
login.login_message = 'Login required!'
login.refresh_view = 'auth_route.login'


def create_app(env: str = None) -> Flask:
    """Flask Application Factory

    Keyword Arguments:
    env: Name of the configuartion to launch - 
        'development', 'testing', 'production'

    Returns:
        Flask() -- The Flask app
    """
    from app.config import config_by_name

    app = Flask(__name__)
    if environ.get('FLASK_ENV') == 'production':
        app.wsgi_app = ReverseProxied(app.wsgi_app)
    
    app.config.from_object(config_by_name[env or "test"])
    db.init_app(app)   
    migrate.init_app(app, db)
    csrf.init_app(app)
    login.init_app(app)
    principals.init_app(app)
    api.init_app(app)

    from app.routes import register_routes

    register_routes(api, app)
    

    # In testing environemt need to mimic setting Flask_Principals permissions
    if environ.get('FLASK_ENV') == 'test':
        @app.before_request
        def determine_identity() -> None:
            identity_changed.send(
                current_app._get_current_object(),
                identity=Identity('test@test.com'))


    # Health test
    @app.route("/health")
    def health() -> Response:
        return jsonify("healthy")

    return app

def database_manager(env: str = None) -> Flask:
    """ Create App to Manager Databases

    This function is used in conjunction with
    the script manage_db.py to record database
    migrations and perform upgrades.
    
    Keyword Arguments:
    env: Name of the configuartion to launch - 
        'development', 'testing', 'production'

    Returns:
        Flask() -- The Flask app

    """

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

    db.init_app(app)

    migrate.init_app(app, db)
    
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    return manager