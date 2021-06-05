import time
import logging
logger = logging.getLogger("execution_time_log")
def exec_time(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        try:
            return func(*args, **kwargs)
        finally:
            end_time = time.time()
            logger.info("{}:{}".format(func.__qualname__, end_time-start_time))
    return inner