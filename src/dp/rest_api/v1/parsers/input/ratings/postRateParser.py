# coding: utf-8
__author__ = 'Miso'

from webargs import fields, validate

ratings = [0, 1, 2, 3, 4, 5, 6]
rating_flag = [1, 2]
changed_flag = [0, 1]

post_user_rate_parser = {
    'rating_type': fields.Int(required=True, validate=validate.OneOf(ratings)),
    'created': fields.Int(required=True),
    'updated': fields.Int(required=True),
    'url': fields.Str(required=True, missing=None),
    'category_type': fields.Int(required=True, validate=validate.OneOf(ratings)),
    'rating_flag': fields.Int(required=True, validate=validate.OneOf(rating_flag)),
    'tab': fields.Int(required=False, default=0),
    'changed': fields.Int(required=True, default=0, validate=validate.OneOf(changed_flag)),
    'rateFrom': fields.Int(required=False, default=0, validate=validate.OneOf(ratings))
}
