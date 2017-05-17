# coding: utf-8
__author__ = 'Miso'

from db.dbInit import db


class RateTypes(db.Model):
	__tablename__ = 'rate_types'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(16))
