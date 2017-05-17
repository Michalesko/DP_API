# coding: utf-8
__author__ = 'Miso'

from datetime import datetime
from flask_restful import Resource
from webargs.flaskparser import use_args

from rest_api.v1.parsers.input.loggs.postLogItemParser import post_log_item_parser
from rest_api.v1.parsers.output.loggs.logParser import LogItemSchema
from db.model import db, LogItem


class LoggsHandler(Resource):

    @use_args(post_log_item_parser)
    def post(self, args):

        timeS = str(args['timestamp'])
        newTime = datetime.fromtimestamp(int(timeS[0:len(timeS) - 3]))

        new_log = LogItem(
            tab_id=args['tab_id'],
            session_id=args['session_id'],
            window_id=args['window_id'],
            time=newTime,
            event=args['event'],
            url=args['url'],
            path=args['path'],
            domain=args['domain'],
            index_from=args['index_from'],
            index_to=args['index_to'],
            user_id=args['user_id']
        )

        db.session.add(new_log)
        db.session.commit()

        id = str(new_log.id)
        response = LogItemSchema().dump(new_log)

        db.session.close()
        return response, 201, {'Location': '/api/v1/logs/' + id}
