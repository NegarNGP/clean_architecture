from flask import Flask
from .site.route import site
from .api.route import api

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api)
    app.register_blueprint(site)
    return app