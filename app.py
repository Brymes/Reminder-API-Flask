from flask import Flask
from flask_restful import Api

from config import Config
from extensions import db
from api.routes import initialize_routes


def register_extensions(app):
    db.init_app(app)


def register_resources(app):
    api = Api(app)
    initialize_routes(api)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_resources(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
