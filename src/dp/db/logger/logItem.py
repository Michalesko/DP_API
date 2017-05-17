# coding: utf-8
__author__ = 'Miso'

from db.dbInit import db


class LogItem(db.Model):
    __tablename__ = 'log_item'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    tab_id = db.Column(db.Integer)
    session_id = db.Column(db.String(64))
    time = db.Column(db.TIMESTAMP)
    window_id = db.Column(db.Integer)
    event = db.Column(db.String(16))
    url = db.Column(db.String(64))
    domain = db.Column(db.String(32))
    path = db.Column(db.String(64))
    index_to = db.Column(db.Integer)
    index_from = db.Column(db.Integer)
