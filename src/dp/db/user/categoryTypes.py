# coding: utf-8
__author__ = 'Miso'

from db.dbInit import db


class CategoryTypes(db.Model):
	__tablename__ = 'category_types'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(16))
