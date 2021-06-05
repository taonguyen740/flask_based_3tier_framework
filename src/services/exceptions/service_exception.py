from src.exceptions import BaseException
from .service_error_code import ServiceErrorCode


class ServiceException(BaseException):
    def __init__(self, error: ServiceErrorCode, message=None, message_format=None):
        if not isinstance(error, ServiceErrorCode):
            raise ValueError("error must be instance of ServiceErrorCode")
        super().__init__(error, message=message, message_format=message_format)
