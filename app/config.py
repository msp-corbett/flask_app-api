""" App Configuration """
from os import environ, path
from typing import List, Type


class BaseConfig:
    CONFIG_NAME = "base"
    USE_MOCK_EQUIVALENCY = False
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TRAP_HTTP_EXCEPTIONS = True


class DevelopmentConfig(BaseConfig):
    CONFIG_NAME = "development"
    SECRET_KEY = environ.get('DEV_SECRET_KEY', 'TheyTried2MakeMeG02Rhab')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False
    
    basedir = path.abspath(path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = environ.get('DEV_SQLALCHEMY_DATABASE_URI') or \
        'sqlite:///' + path.join(basedir, 'app.db')


class TestingConfig(BaseConfig):
    CONFIG_NAME = "test"
    SECRET_KEY = environ.get("TEST_SECRET_KEY", "KingJeremyTheWicked")
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True
    LOGIN_DISABLED = True
    SQLALCHEMY_DATABASE_URI =  ""


class ProductionConfig(BaseConfig):
    CONFIG_NAME = "production"
    SECRET_KEY = environ.get("PROD_SECRET_KEY", "BikiniBott0m5LagerT0p5")
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = environ.get('PROD_SQLALCHEMY_DATABASE_URI')


EXPORT_CONFIGS: List[Type[BaseConfig]] = [
    DevelopmentConfig,
    TestingConfig,
    ProductionConfig,
]

config_by_name = {cfg.CONFIG_NAME: cfg for cfg in EXPORT_CONFIGS}
