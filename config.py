import os
from urllib import parse

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get("postgres://pvmwvkgbmpdfvp:123d0a1b1642479e9927da70bd4f180e947e448336bb04dbd3b2d81217a6549d@ec2-54-163-234-99.compute-1.amazonaws.com:5432/d5ceo39rqj5ph3")
    SQLALCHEMY_TRACK_MODIFICATIONS = False