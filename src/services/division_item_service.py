from src.daos import FactoryInterface
from .base_service import BaseService
from .exceptions import ServiceErrorCode, ServiceException


class DivisionItemService(BaseService):
    def __init__(self, dao_factory: FactoryInterface = None):
        super().__init__(dao_factory)
        self.division_item_dao = self.dao_factory.create_division_item_dao()

    def get_division_items(self, parrent_code):
        """区分項目取得する
        Args:
            parrent_code (str): 親区分コード

        Returns:
            list(dict[str, str]): 区分項目

        Examples:
            >>> get_division_items("STATUS")
            [
                {
                    "code": "STA01",
                    "text": "ステータス１"
                },
                {
                    "code": "STA02",
                    "text": "ステータス２"
                }
            ]
        """
        if parrent_code in ["STATUS"]:
            division_items = self.division_item_dao.get_division_items(
                parrent_code)
            return division_items
        else:
            raise ServiceException(
                ServiceErrorCode.INVALID_DIVISION_PARRENT_CODE)
