# coding: utf-8
__author__ = 'Miso'

import sys
sys.path.append('..')

from flask import Flask

from db.model import *
from db.dbInit import db
from db.redis.redisInit import redis_store

from config import MYSQL_URL
from config import REDIS_URL
from server import BaseServer

from api.engine import RecommenderEngine


recommendation_engine = RecommenderEngine()
application = Flask(__name__, template_folder='templates')

application.debug = True
application.secret_key = 'secret'
application.config.update({
    'SQLALCHEMY_DATABASE_URI': MYSQL_URL,
    'SQLALCHEMY_TRACK_MODIFICATIONS': False
})
application.config['REDIS_URL'] = REDIS_URL

server = BaseServer(application, recommendation_engine)

if __name__ == '__main__':
    application.app_context().push()
    db.init_app(application)

    db.create_all()
    redis_store.init_app(application)
    application.run(host="127.0.0.1", port=5000)
