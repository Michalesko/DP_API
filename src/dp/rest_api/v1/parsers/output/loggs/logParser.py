# coding: utf-8
__author__ = 'Miso'

from marshmallow import Schema, fields


class LogItemSchema(Schema):
    id = fields.Integer()
    tab_id = fields.Integer()
    session_id = fields.String()
    window_id = fields.Integer()
    event = fields.String()
    url = fields.String()
    user_id = fields.Integer()
    timestamp = fields.DateTime()
    index_to = fields.Integer()
    index_from = fields.Integer()
