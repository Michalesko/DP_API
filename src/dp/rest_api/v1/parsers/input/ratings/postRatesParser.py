# coding: utf-8
__author__ = 'Miso'

from marshmallow import Schema, fields
from webargs import validate

ratings = [1, 2, 3, 4, 5, 6]
rating_flag = [1, 2]


class UserIntialRatingParser(Schema):
    rating_type = fields.Int(
        required=True,
        validate=validate.OneOf(rating_flag)
    )
    rating_flag = fields.Int(
        required=True,
        validate=validate.OneOf(rating_flag)
    )
    category_type = fields.Int(
        required=True,
        validate=validate.OneOf(ratings)
    )
    time = fields.DateTime(required=True)
    url = fields.Str(required=True, missing=None)

    class Meta:
        strict = True
