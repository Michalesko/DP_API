# coding: utf-8
__author__ = 'Miso'

from marshmallow import Schema, fields


class UserGoalSchema(Schema):
    id = fields.Integer()
    session_id = fields.String()
    user_id = fields.Integer()
    goal = fields.Integer()
    flag = fields.Integer()
