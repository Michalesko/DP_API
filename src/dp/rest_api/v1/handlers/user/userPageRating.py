# coding: utf-8
__author__ = 'Miso'

from flask_restful import Resource
from db.model import db, UserRating, CategoryTypes
from rest_api.errors.users import err_user_not_exist
from webargs.flaskparser import use_args
from sqlalchemy import and_

import rest_api.v1.parsers.input.ratings as parser


class UserPageRating(Resource):

    def __init__(self, engine):
        self.recom_engine = engine

    @use_args(parser.get_rate_parser)
    def get(self, args, userId):

        webpage = args['url']
        userPages = UserRating.query.filter(and_(UserRating.user_id == userId, UserRating.rate_flag != 3)).all()
        if not userPages:
            return err_user_not_exist

        print webpage
        for page in userPages:
            if page.url == str(webpage) or\
               page.url in str(webpage) or\
               ('www' in page.url and '.'.join(page.url.split('.')[1:]) in str(webpage)):

                category_rate = CategoryTypes.query.filter(CategoryTypes.id == page.category_id).first()
                return {'rate_id': page.category_id, 'category_rate': category_rate.name, 'rate_type': 'own'}, 200

        # anyNeighbour = UserRating.query.filter(UserRating.url == args['url']).first()
        # if not anyNeighbour:
        #     return {'rate_id': 0, 'category_rate': "http://sample.com"}, 200

        all_ratings = self.recom_engine.get_all_users_ratings()
        self.recom_engine.generate_similarities(all_ratings)
        rate = self.recom_engine.generate_rating(userId, webpage)
        out = {"rate_id": rate, 'rate_type': 'recom'}

        print rate
        if rate != 0:
            category_rate = CategoryTypes.query.filter(CategoryTypes.id == rate).first()

            cat = {'category_rate': category_rate.name}
        else:
            cat = {'category_rate': 'http://example.com'}

        db.session.close()
        out.update(cat)
        return out, 200
