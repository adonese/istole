import os
from urllib import parse
import psycopg2

parse.uses_netloc.append("postgres")
url = parse.urlparse(os.environ["postgres://pvmwvkgbmpdfvp:123d0a1b1642479e9927da70bd4f180e947e448336bb04dbd3b2d81217a6549d@ec2-54-163-234-99.compute-1.amazonaws.com:5432/d5ceo39rqj5ph3"])

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)