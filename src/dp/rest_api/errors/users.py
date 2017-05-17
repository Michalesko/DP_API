# coding: utf-8
__author__ = 'Miso'

import json

err_user_not_exist = json.dumps({"error_code": 102, "error_message": "User with this id does not exists."}), 400
