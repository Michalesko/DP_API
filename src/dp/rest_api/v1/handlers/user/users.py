# coding: utf-8
__author__ = 'Miso'


from flask_restful import Resource
from webargs.flaskparser import use_args

import rest_api.v1.parsers.input.user as userParser
from rest_api.v1.parsers.output.user.userParser import UserSchema
from db.model import db, User
from rest_api.errors.users import err_user_not_exist


class UsersHandlerOne(Resource):

    def get(self, userId):

        user = User.query.filter(User.id == userId).first()
        if not user:
            return err_user_not_exist
        response, errors = UserSchema().dump(user)
        db.session.close()

        return response, 200

    @use_args(userParser.put_users_parser)
    def put(self, args, userId):
        user = User.query.filter(User.id == userId).first()
        if args.get('name'):
            user.name = args['name']
        if args.get('skills'):
            user.skills = args['skills']

        db.session.add(user)
        db.session.commit()
        response, errors = UserSchema().dump(user)
        db.session.close()

        return response, 200

    def delete(self, userId):

        user = User.query.filter(User.id == userId).first()
        db.session.delete(user)
        db.session.commit()
        db.session.close()
        return None, 204


class UsersHandler(Resource):

    @use_args(userParser.post_users_parser)
    def post(self, args):

        new_user = User(extID=args['extId'])
        db.session.add(new_user)
        db.session.commit()
        uid = str(new_user.id)
        response = UserSchema().dump(new_user)

        db.session.close()
        return response, 201, {'Location': '/api/v1/users/' + uid}
