def register_routes(api, app):
    from app.frontend import register_routes as attach_frontend
    #from app.backend import register_routes as attach_backend


    attach_frontend(app)
    #attach_backend(api, app)
    