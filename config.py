"""Conatain App configurations."""
import os


class Config(object):
    """Model base config object that can inherited by other configs."""

    SECRET_KEY = os.environ.get('SECRET') or "secretkey"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    TESTING = False
    DEVELOPMENT = False


class Development(Config):
    """Model Development enviroment config object."""

    DEBUG = True
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE') or \
        'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class Production(Config):
    """Model Production enviroment config object."""

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class Testing(Config):
    """Model Testing enviroment config object."""

    DEBUG = True
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE') or \
        'sqlite:///:memory:'


class Staging(Development):
    """Model Staging enviroment config object."""

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


configuration = {
    "Testing": Testing,
    "Development": Development,
    "Production": Production,
    "Staging": Staging
}
