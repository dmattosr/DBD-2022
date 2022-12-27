# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os

path = os.getcwd()


class Config(object):

    basedir = os.path.abspath(os.path.dirname(__file__))

    # Set up the App SECRET_KEY
    # SECRET_KEY = config('SECRET_KEY'  , default='S#perS3crEt_007')
    SECRET_KEY = os.getenv('SECRET_KEY', 'S#perS3crEt_007')

    # This will create a file in <app> FOLDER
    if os.getenv('DB_ENGINE'):
        # PostgreSQL database
        SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
            os.getenv('DB_ENGINE', 'postgresql'),
            os.getenv('DB_USERNAME', 'appseed_db_usr'),
            os.getenv('DB_PASS', 'pass'),
            os.getenv('DB_HOST', 'localhost'),
            os.getenv('DB_PORT', 5432),
            os.getenv('DB_NAME', 'appseed_db')
        )
    else:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
            os.path.join(basedir, 'db.sqlite3')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Assets Management
    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')

    MAX_CONTENT_LENGTH = os.getenv('MAX_CONTENT_LENGTH', 5) * 1024 * 1024

    UPLOAD_FOLDER = os.path.join(path, 'uploads')

    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'pdf', 'docx', 'xlsx', 'xls'])

    if not os.path.isdir(UPLOAD_FOLDER):
        os.mkdir(UPLOAD_FOLDER)

    APP_COMPANY = os.getenv('APP_NAME', 'MINSA')
    APP_NAME = os.getenv('APP_NAME', 'CITAS@LINEA')
    APP_FULLNAME = os.getenv('APP_FULLNAME', 'Gestión de citas en línea')


class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600


class DebugConfig(Config):
    DEBUG = True


# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig,
}
