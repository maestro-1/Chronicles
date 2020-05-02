import os


Secret_Key = os.environ.get("SECRET_KEY")
Database_Url = os.environ.get("DATABASE_URL")
# Database_Url = os.environ.get("DATABASE_URL")


class BaseConfig:
    SECRET_KEY = Secret_Key
    SQLALCHEMY_DATABASE_URI = Database_Url
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')


class TestConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class ProductionConfig(BaseConfig):
    DEBUG = False
