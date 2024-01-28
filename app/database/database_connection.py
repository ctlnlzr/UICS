import sqlite3
from flask import g
import os


def close_connection():
    connection = g.pop('conn', None)

    if connection is not None:
        connection.close()


def get_connection():
    if 'conn' not in g:
        project_root = os.path.dirname(os.path.realpath(__file__))
        database = os.path.join(project_root, 'conversions.db')

        g.conn = sqlite3.connect(database)

    return g.conn


def init_app(app):
    app.teardown_appcontext(close_connection)
