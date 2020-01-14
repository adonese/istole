import os
from urllib import parse


class Config(object):
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
