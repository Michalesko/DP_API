# coding: utf-8
__author__ = 'Miso'

from webargs import fields


get_rate_parser = {
    'url': fields.Str(required=True, location='query'),
    'tab': fields.Int(required=True, location='query')
}
