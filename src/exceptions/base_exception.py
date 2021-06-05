from enum import Enum


class BaseException(Exception):
    def __init__(self, error: Enum, message=None, message_format=None):

        self.error = error
        message = message or error.value
        if message_format:
            message = message.format(**message_format)
        self.message = message
        super().__init__(message)
