# coding: utf-8
__author__ = 'Miso'

from webargs import fields


post_users_parser = {
    'extId': fields.Str(required=False, validate=lambda val: len(val) >= 0)
}
