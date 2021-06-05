import json
from . import DivisionItemDaoInterface
from ..base_dao import BaseDao
from src.database import Database
from src.daos.exceptions import DaoErrorCode, DaoException
from datetime import datetime


class RdsDivisionItemDao(DivisionItemDaoInterface, BaseDao):
    def __init__(self):
        BaseDao.__init__(self)
        self.db = Database()

    def get_division_items(self, parrent_code):
        try:
            query = """SELECT code, text from M_DIVISION_ITEMS WHERE parent_code = :parrent_code """
            res = self.execute_to_dict(query, {'parrent_code': parrent_code})
            return res
        finally:
            self.close()
