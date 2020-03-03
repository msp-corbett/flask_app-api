from . import home_route

@home_route.route("/")
@home_route.route("/home")
def index():
    """ Home page """

    return "<h1>Home page</h1>"
