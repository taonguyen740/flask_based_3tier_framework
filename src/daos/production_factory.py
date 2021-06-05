from .factory_interface import FactoryInterface
from .user_dao import UserDaoInterface, RdsUserDao
from .division_item_dao import RdsDivisionItemDao, DivisionItemDaoInterface


class ProductionFactory(FactoryInterface):
    def create_user_dao(self) -> UserDaoInterface:
        return RdsUserDao()

    def create_division_item_dao(self) -> DivisionItemDaoInterface:
        return RdsDivisionItemDao()
