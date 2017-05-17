# coding: utf-8
__author__ = 'Miso'

from flask_restful import Resource
from db.model import db, UserRating
from rest_api.errors.users import err_user_not_exist


class UserPages(Resource):

    def get(self, userId):

        response = []
        userPages = UserRating.query.filter(UserRating.user_id == userId).all()
        if not userPages:
            return err_user_not_exist

        for page in userPages:
            response.append(page.url)

        db.session.close()
        return response, 200
