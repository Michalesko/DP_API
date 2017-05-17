# coding: utf-8
__author__ = 'Miso'

from webargs import fields

post_users_time_parser = {
    'goalTime': fields.Float(required=True),
    'nonGoalTime': fields.Float(required=True)
}
