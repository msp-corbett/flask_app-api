# flask_app-api
A web application supported by an API powered by Flask.

## Design
The design has evolved from my experience with making applications with Flask,
and influenced by other projects such as Flaskerize and the Flask Megatutorial.

Outline:

application.py
app/
    |-static/
    |-frontend/
        |-blue_print_1
        |-blue_print_2
    |-backend/
        |-api
            |-resouce/
                |-widget_a
                |-widget_b
            |-api-error
            |-utility
        |-auth
    |-reverse_proxy/

### Front End
This is intended to house Blueprints whos views are user-facing and interactive.

### Back End
This is intended to house the API routes for all the widgets of the data model.

## Links
* https://github.com/pallets/flask
* https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
* https://github.com/apryor6/flaskerize/
