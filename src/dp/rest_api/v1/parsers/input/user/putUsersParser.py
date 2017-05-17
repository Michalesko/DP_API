# coding: utf-8
__author__ = 'Miso'

from webargs import fields, validate

skillsOptions = ('beginner', 'advanced', 'professional')

put_users_parser = {
    'name': fields.Str(required=False, validate=lambda val: len(val) >= 0, missing='user'),
    'skills': fields.Str(required=False, validate=validate.OneOf(skillsOptions), missing='beginner'),
    'extId': fields.Str(required=False, validate=lambda val: len(val) >= 0)
}
