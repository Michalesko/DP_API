# coding: utf-8
__author__ = 'Miso'

from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Integer()
    extID = fields.String()
    name = fields.String()
    skills = fields.String()
    goal = fields.Integer()
