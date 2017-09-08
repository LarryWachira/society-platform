"""Main app module."""
from flask import Flask, jsonify

from api.models import db

try:
    from .config import configuration
except ImportError:
    from config import configuration


def create_app(enviroment="Development"):
    """Factory Method that creates an instance of the app with the given config.

    Args:
        enviroment (str): Specify the configuration to initilize app with.
    Returns:
        app (Flask): it returns an instance of Flask.
    """
    app = Flask(__name__)
    app.config.from_object(configuration[enviroment])
    db.init_app(app)

    # handle default 404 exceptions with a custom response
    @app.errorhandler(404)
    def resource_not_found(error):
        response = jsonify(dict(
            error='Not found',
            message='The requested URL was not found on the server.'))
        response.status_code = 404
        return response

    # handle default 500 exceptions with a custom response
    @app.errorhandler(500)
    def internal_server_error(error):
        response = jsonify(dict(
            error='Internal server error',
            message="The server encountered an internal error."))
        response.status_code = 500
        return response

    return app
