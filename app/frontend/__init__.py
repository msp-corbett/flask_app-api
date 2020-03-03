from .home import home_route as home_blueprint
from .help import help_route as help_blueprint
from .error import error_route as error_blueprint

def register_routes(app):
    app.register_blueprint(home_blueprint)
    app.register_blueprint(help_blueprint)
    app.register_blueprint(error_blueprint)

