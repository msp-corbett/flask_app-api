""" Errors module """
from flask import Blueprint

home_route = Blueprint('home', __name__, template_folder='templates')

from . import views