# coding: utf-8
__author__ = 'Miso'

from webargs import fields


post_log_item_parser = {
	'tab_id': fields.Int(required=True),
	'session_id': fields.Str(required=True),
	'window_id': fields.Int(required=True),
	'timestamp': fields.Int(required=True),
	'event': fields.Str(required=True),
	'url': fields.Str(required=False, missing=None),
	'path': fields.Str(required=False, missing=None),
	'domain': fields.Str(required=False, missing=None),
	'index_to': fields.Int(required=False, missing=None),
	'index_from': fields.Int(required=False, missing=None),
	'user_id': fields.Int(required=True)
}
