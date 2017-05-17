# coding: utf-8
__author__ = 'Miso'

from webargs import fields

post_users_goal_parser = {
    'goals': fields.DelimitedList(fields.Int(), required=False),
    'session': fields.Str(required=True)
}
