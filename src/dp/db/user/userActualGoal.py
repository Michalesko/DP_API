# coding: utf-8
__author__ = 'Miso'

from db.dbInit import db


class UserActualGoal(db.Model):
	__tablename__ = 'user_actual_goal'
	id = db.Column(db.Integer, primary_key=True)
	session_id = db.Column(db.String(64))
	user_id = db.Column(db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
	goal = db.Column(db.ForeignKey('category_types.id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
	flag = db.Column(db.Integer)
