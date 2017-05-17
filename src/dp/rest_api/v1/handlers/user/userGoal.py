# coding: utf-8
__author__ = 'Miso'

from flask_restful import Resource
from webargs.flaskparser import use_args

import rest_api.v1.parsers.input.user as userParser
from rest_api.v1.parsers.output.user.userGoalParser import UserGoalSchema
from db.model import db, UserActualGoal


class UserHandlerGoal(Resource):

    @use_args(userParser.post_users_goal_parser)
    def post(self, args, userId):

        userGoals = UserActualGoal.query.filter(UserActualGoal.user_id == userId).all()

        for userGoal in userGoals:
            userGoal.flag = 0
        db.session.commit()

        goals = []

        for i in xrange(len(args['goals'])):
            goals.append(
                db.session.add(
                    UserActualGoal(
                        session_id=args['session'],
                        user_id=userId,
                        goal=int(args['goals'][i]),
                        flag=1
                    )
                )
            )
        db.session.commit()

        response, errors = UserGoalSchema(many=True).dump(goals)
        db.session.close()
        return response, 200
