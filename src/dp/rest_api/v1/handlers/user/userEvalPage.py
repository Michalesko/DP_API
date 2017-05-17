# coding: utf-8
__author__ = 'Miso'

from flask_restful import Resource
from webargs.flaskparser import use_args
from rest_api.v1.parsers.output.user.userEvalParser import UserEvalSchema
import rest_api.v1.parsers.input.ratings as ratingParser
from db.model import db, UserRating
from datetime import datetime


class UserHandlerRuntimeEval(Resource):

    def __init__(self, engine):
        self.recom_engine = engine

    @use_args(ratingParser.post_user_rate_parser)
    def post(self, args, userId):

        timeS = str(args['created'])
        created = datetime.fromtimestamp(int(timeS[0:len(timeS) - 3]))
        timeS = str(args['updated'])
        updated = datetime.fromtimestamp(int(timeS[0:len(timeS) - 3]))

        userRate = UserRating(
            user_id=userId,
            category_id=args['category_type'],
            url=args['url'],
            rate_type=args['rating_type'],
            created=created,
            updated=updated,
            rate_flag=args['rating_flag'],
            tab_id=args['tab'],
            rate_changed=args['changed'],
            rate_from=args['rateFrom']
        )
        db.session.add(userRate)

        db.session.commit()
        rid = str(userRate.id)
        response, errors = UserEvalSchema().dump(userRate)

        db.session.close()
        self.recom_engine.push_rating(userId, args['url'], args['category_type'])

        return response, 201, {'Location': '/api/v1/users/' + str(userId) + '/runeval/' + rid}
