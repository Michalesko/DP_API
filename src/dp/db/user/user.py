# coding: utf-8
__author__ = 'Miso'

from db.dbInit import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, default='user')
    skills = db.Column(db.String(16))
    extID = db.Column(db.String(64))
    registration_date = db.Column(db.TIMESTAMP, default=db.func.now(), nullable=False)

    user_logs = db.relationship("LogItem", backref="user", lazy='dynamic', passive_deletes=True)
