import time
import logging
logger = logging.getLogger("execTimeLogging")
def log_started_at(func_name):
    logger.info("{} STARTED".format(func_name))

def log_end_at(func_name, exec_time):
    logger.info("{} ENDED_IN {}".format(func_name, exec_time))

def exec_time_logging_decorator(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        try:
            log_started_at(func.__qualname__)
            return func(*args, **kwargs)
        finally:
            end_time = time.time()
            # print(func.__qualname__, exec_time)
            log_end_at(func.__qualname__, end_time-start_time)
    return inner