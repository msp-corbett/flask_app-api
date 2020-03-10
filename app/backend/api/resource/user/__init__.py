from flask import Blueprint

user_route = Blueprint('user_route', __name__, template_folder='templates')

from . import views