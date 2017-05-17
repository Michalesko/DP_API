# coding: utf-8
__author__ = 'Miso'

from marshmallow import fields, Schema


class UserPagesSchema(Schema):
    url = fields.String()
