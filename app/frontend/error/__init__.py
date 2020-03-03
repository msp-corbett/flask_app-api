""" Errors module """
from flask import Blueprint

error_route = Blueprint('error', __name__, template_folder='templates')

from . import views