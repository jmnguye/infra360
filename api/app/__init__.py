from flask import Flask
from flask_restx import Api
from app.resources.domains import api as Domains


def create_app():
    app = Flask(__name__)

    api = Api(app)
    api.add_namespace(Domains)

    return app
