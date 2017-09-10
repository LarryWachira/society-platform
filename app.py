""" Main app module. """
import os

from api.endpoints.activities import ActivitiesAPI
from api.endpoints.point import PointResource
from api.endpoints.societies import SocietyResource
from api.endpoints.users import UserAPI
from api.models import db
from flask import Flask, jsonify
from flask_cors import CORS
from flask_restplus import Api
from flask_sslify import SSLify

try:
    from .config import configuration
except ImportError:
    from config import configuration


def create_app(environment="Development"):
    """Factory Method that creates an instance of the app with the given config.

    Args:
        environment (str): Specify the configuration to initilize app with.

    Returns:
        app (Flask): it returns an instance of Flask.
    """
    app = Flask(__name__)
    app.config.from_object(configuration[environment])
    db.init_app(app)

    api = Api(
        app=app,
        default='Api',
        default_label="Available Endpoints",
        title='🗣️ Open-Platform Api 😱',
        version='1.0',
        description="""Open-Platform Api Endpoint Documentation 📚""")

    # to redirect all incoming production requests to https
    if environment.lower() == "production":
        sslify = SSLify(app, subdomains=True, permanent=True)

    # enable cross origin resource sharing
    CORS(app)

    # activities endpoints
    api.add_resource(
        ActivitiesAPI, '/api/v1/activities', '/api/v1/activities/',
        endpoint='activities'
    )

    # user endpoints
    api.add_resource(
        UserAPI, '/api/v1/user/profile', '/api/v1/user/profile/',
        endpoint='user_info'
    )

    # society endpoints
    api.add_resource(
        SocietyResource, "/api/v1/societies", "/api/v1/societies/",
        endpoint="society"
    )

    api.add_resource(
        SocietyResource,
        "/api/v1/societies/<string:society_id>",
        "/api/v1/societies/<string:society_id>/",
        endpoint="society_detail"
    )

    # points endpoints
    api.add_resource(PointResource, '/api/v1/points/', '/api/v1/points')

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
