# coding: utf-8
__author__ = 'Miso'

import os

from db.model import db


if not os.path.isdir("migrations"):
    os.system("python -m db.model db init")

os.system("python -m db.model db migrate")
os.system("python -m db.model db upgrade")


if __name__ == '__main__':
    db.create_all()
