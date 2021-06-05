import os
from abc import ABC
from src.daos import FactoryInterface, ProductionFactory
from src.utils import custom_logging
import traceback


class BaseService(ABC):
    def __init__(self, dao_factory: FactoryInterface = None):
        exclude = []
        if dao_factory is None:
            self.dao_factory = ProductionFactory()
        else:
            self.dao_factory = dao_factory
        for attr in dir(self):
            if callable(getattr(self, attr)) and attr[0] != "_" and attr not in exclude:
                if os.environ.get("EXEC_TIME_LOG_ENABLED"):
                    try:
                        setattr(self, attr, custom_logging.exec_time_logging_decorator(
                            getattr(self, attr)))
                    except Exception as e:
                        traceback.print_exc()
