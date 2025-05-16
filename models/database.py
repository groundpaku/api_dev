#! /usr/bin/python3
# coding: utf-8

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.pool import NullPool

db = SQLAlchemy()


def init_db(app):
#     app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
#             "poolclass": NullPool
#             }
    db.init_app(app)
