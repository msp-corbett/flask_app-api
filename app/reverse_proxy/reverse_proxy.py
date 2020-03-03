""" Methods to handle Reverse Proxy """

class ReverseProxied():
    """ Set the URL Scheme for server-generated URLs

    If deployed to server behind a load balancer e.g.
    Azure app -> gunicorn + nginx
    The function flask.url_for will generate URLs with
    the 'http' scheme instead of the desired 'https'

    Need to use the WSGI middleware to set the appropriate scheme.

    Solution lifted from:
        https://stackoverflow.com/questions/14810795/flask-url-for-generating-http-url-instead-of-https


    """
    def __init__(self, app):
        self.app = app

    def __call__(self, env, start_response):
        scheme = env.get('HTTP_X_FORWARDED_PROTO')
        if scheme:
            env['wsgi.url_scheme'] = scheme
        return self.app(env, start_response)