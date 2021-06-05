from abc import ABC, abstractmethod


class DivisionItemDaoInterface(ABC):
    @abstractmethod
    def get_division_items(self, code):
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
        raise NotImplementedError
