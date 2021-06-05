from src.exceptions import BaseException
from src.daos.exceptions.dao_error_code import DaoErrorCode


class DaoException(BaseException):
    def __init__(self, error: DaoErrorCode, message=None, message_format=None):
        if not isinstance(error, DaoErrorCode):
            raise ValueError("error must be instance of DaoErrorCode")
        super().__init__(error, message=message, message_format=message_format)
