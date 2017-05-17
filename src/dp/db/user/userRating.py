# coding: utf-8
__author__ = 'Miso'

from db.dbInit import db


class UserRating(db.Model):
	__tablename__ = 'user_rating'
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
	category_id = db.Column(db.ForeignKey('category_types.id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
	url = db.Column(db.String(64))
	rate_type = db.Column(db.ForeignKey('rate_types.id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
	created = db.Column(db.TIMESTAMP, default=db.func.now())
	updated = db.Column(db.TIMESTAMP, default=db.func.now())
	rate_changed = db.Column(db.Integer, default=0)
	rate_flag = db.Column(db.ForeignKey('rate_flag.id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
	rate_from = db.Column(db.Integer, default=0)
	tab_id = db.Column(db.Integer)
