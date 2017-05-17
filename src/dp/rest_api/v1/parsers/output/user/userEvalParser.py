# coding: utf-8
__author__ = 'Miso'

from marshmallow import Schema, fields


class UserEvalSchema(Schema):
    id = fields.Integer()
    user_id = fields.Integer()
    category_id = fields.Integer()
    rate_type = fields.Integer()
    rate_flag = fields.Integer()
    url = fields.String()
    tab_id = fields.Integer()
    created = fields.DateTime()
    updated = fields.DateTime()
    rate_changed = fields.Integer()
    rate_from = fields.Integer()
