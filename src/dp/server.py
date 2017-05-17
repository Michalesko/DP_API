# coding: utf-8
__author__ = 'Miso'

from flask_restful import Api
from webargs.flaskparser import parser, abort
from flask import render_template

import sys
sys.path.append('..')

from db.model import db
import rest_api.v1.handlers.user as userHandler
from rest_api.v1.handlers.logger.logger import LoggsHandler


class BaseServer(object):

    def __init__(self, app, recom_engine):

        api_no_oauth = Api(app)

        # API USERS SERVICES
        api_no_oauth.add_resource(userHandler.UsersHandler, '/api/v1/users')
        api_no_oauth.add_resource(userHandler.UsersHandlerOne, '/api/v1/users/<int:userId>')
        api_no_oauth.add_resource(userHandler.UserHandlerGoal, '/api/v1/users/<int:userId>/goal')
        api_no_oauth.add_resource(userHandler.UserHandlerTime, '/api/v1/users/<int:userId>/time')
        api_no_oauth.add_resource(userHandler.UserHandlerRuntimeEval,
                                  '/api/v1/users/<int:userId>/runeval', resource_class_kwargs={'engine': recom_engine})
        api_no_oauth.add_resource(userHandler.UserPages, '/api/v1/users/<int:userId>/webpages')
        api_no_oauth.add_resource(userHandler.UserPageRating, '/api/v1/users/<int:userId>/recom',
                                  resource_class_kwargs={'engine': recom_engine})
        api_no_oauth.add_resource(LoggsHandler, '/api/v1/logs')

        @parser.error_handler
        def handle_request_parsing_error(err):
            """webargs error handler that uses Flask-RESTful's abort function to return
            a JSON error response to the client.
            """
            # raise
            abort(err.status_code, errors=err.messages)

        @app.errorhandler(404)
        def page_not_found(error):
            return render_template('404.html'), 404

        @app.errorhandler(500)
        def internal_error(error):
            print error
            db.session.rollback()
            db.session.close()
            return "Internal server error", 500

        @app.after_request
        def after_request(response):
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
            response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
            return response
