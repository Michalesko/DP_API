# coding: utf-8
__author__ = 'Miso'

from flask_restful import Resource
from webargs.flaskparser import use_args

import rest_api.v1.parsers.input.user as userParser
from db.model import db, UserTime


class UserHandlerTime(Resource):

    @use_args(userParser.post_users_time_parser)
    def post(self, args, userId):

        userLogTime = UserTime.query.filter(UserTime.user_id == userId).first()
        if userLogTime:
            userLogTime.goalTime = userLogTime.goalTime + args['goalTime']
            userLogTime.nonGoalTime = userLogTime.nonGoalTime + args['nonGoalTime']
            db.session.add(userLogTime)
        else:
            newLog = UserTime(
                user_id=userId,
                goalTime=args['goalTime'],
                nonGoalTime=args['nonGoalTime']
            )
            db.session.add(newLog)
        db.session.commit()
        db.session.close()
        return {}, 200
