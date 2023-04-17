import os

from dotenv import load_dotenv

load_dotenv()


def db_uri_replace():
    """Troca a URI do banco de dados"""
    uri = os.environ.get('DATABASE_URL')
    if uri and uri.startswith('postgres://'):
        uri = uri.replace('postgres://', 'postgresql://', 1)
    return uri


class Config:
    SQLALCHEMY_DATABASE_URI = db_uri_replace()
    API_KEY = os.environ.get('API_KEY')
    URL = os.environ.get('URL')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    # MAIL_SERVER = os.environ.get('MAIL_SERVER')
    # MAIL_PORT = os.environ.get('MAIL_PORT')
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

