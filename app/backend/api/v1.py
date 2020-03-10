from flask import Blueprint
from flask_restful import Api
from app.backend.resource.user import *
from .widget_x import *
from .widget_y import *

API_VERSION_V1 = 1.0
API_VERSION = API_VERSION_V1

api_v1_bp = Blueprint(
    'api_v1',
    __name__,
    url_prefix=f"/api/v{API_VERSION}")

api_v1 = Api(api_v1_bp)