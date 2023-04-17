import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from config import Config

Base = declarative_base()

logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')


def get_db_session():
    """Cria uma sessão de banco de dados"""
    engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    logging.info('Database session created')

    return Session()
