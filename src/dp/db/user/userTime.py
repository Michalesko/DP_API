# coding: utf-8
__author__ = 'Miso'

from db.dbInit import db


class UserTime(db.Model):
    __tablename__ = 'user_time'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    goalTime = db.Column(db.Float)
    nonGoalTime = db.Column(db.Float)
