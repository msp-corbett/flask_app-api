""" Help module """
from flask import Blueprint

help_route = Blueprint('help', __name__, template_folder='templates')

from . import views