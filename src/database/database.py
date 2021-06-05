import os
import logging
import sqlalchemy
from threading import Lock
from sqlalchemy.orm import sessionmaker, scoped_session


class SingletonMeta(type):
    """
    Lock object that will be used to synchronize threads during
    first access to the Singleton.
    """
    _instance = None
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        # sync between threads
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Database(metaclass=SingletonMeta):
    def __init__(self, app=None, uri=None):
        try:
            logger = logging.getLogger(__name__)
            if not uri:
                if app:
                    uri = app.config.get("SQLALCHEMY_DATABASE_URI")
                    pool_recycle = app.config.get(
                        "SQLALCHEMY_POOL_RECYCLE", 3600)
                elif os.environ.get("SQLALCHEMY_DATABASE_URI"):
                    uri = os.environ.get("SQLALCHEMY_DATABASE_URI")
                    pool_recycle = os.environ.get(
                        "SQLALCHEMY_POOL_RECYCLE", 3600)
            if not uri:
                raise ValueError(
                    "Invalid enviroment variable SQLALCHEMY_DATABASE_URI.")
            logger.info("Init connection with database...")
            self.engine = sqlalchemy.create_engine(
                uri, pool_recycle=pool_recycle)
            self.Session = scoped_session(sessionmaker(bind=self.engine))
            logger.info(
                "Database connection established succeed to {}\n".format(uri))
        except Exception as e:
            logger.exception(
                "Unexpected error! Could not connect to database")
            raise e

    @staticmethod
    def to_dict(result_proxy):
        return [dict(r.items()) for r in result_proxy]
