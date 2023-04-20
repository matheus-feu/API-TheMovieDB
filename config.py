import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


def db_uri_replace():
    """Troca a URI do banco de dados"""
    uri = os.environ.get('DATABASE_URL')
    if uri and uri.startswith('postgres://'):
        uri = uri.replace('postgres://', 'postgresql://', 1)
    return uri


@dataclass
class Config:
    SQLALCHEMY_DATABASE_URI = db_uri_replace()
    API_KEY = os.environ.get('API_KEY')
    URL = os.environ.get('URL')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    TOKEN_API_V4_AUTH = os.environ.get('TOKEN_API_V4_AUTH')
    ACCESS_TOKEN_EXPIRE_MINUTES = 30


@dataclass
class ElasticSearchConfig:
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    ELASTICSEARCH_INDEX: str = 'logs_api'
