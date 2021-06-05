from abc import ABC, abstractmethod
from .user_dao import UserDaoInterface
from .division_item_dao import DivisionItemDaoInterface


class FactoryInterface(ABC):
    @abstractmethod
    def create_user_dao(self) -> UserDaoInterface:
        raise NotImplementedError

    @abstractmethod
    def create_division_item_dao(self) -> DivisionItemDaoInterface:
        raise NotImplementedError
