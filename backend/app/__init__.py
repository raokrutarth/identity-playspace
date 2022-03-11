from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import settings
from typing import FrozenSet

db = SQLAlchemy()


class Config:
    SECRET_KEY = settings.app_secret
    ADMINS: FrozenSet[str] = frozenset()
    SQLALCHEMY_DATABASE_URI = settings.pg_connection_uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False if settings.in_production else True


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    return app


app = create_app()
from app.api.v1 import users
