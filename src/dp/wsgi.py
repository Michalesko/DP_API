# coding: utf-8
__author__ = 'Miso'

from app import application
from db.model import db
from db.redis.redisInit import redis_store


application.app_context().push()
db.init_app(application)
redis_store.init_app(application)

if __name__ == '__main__':
    print "Starting wsgi..."
    db.create_all()

    application.run()
