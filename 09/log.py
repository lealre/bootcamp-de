from loguru import logger
from sys import stderr
from functools import wraps

# remove all sink
logger.remove()

# writes INFO and higher level log messages to the standard error stream
logger.add(
    sink = stderr,
    format= '{time} <r>{level}</r> <g>{message}</g> {file}',
    level = 'INFO'
)

# creates file_log.log
logger.add(
                "09/log_file.log",
                format="{time} {level} {message} {file}",
                level="INFO"
            )

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kargs):
        logger.info(f'Funtion {func.__name__} called with args {args} and kargs {kargs}')
        try:
            result = func(*args, **kargs)
            logger.info(f'Function {func.__name__} returned {result}')
            return result
        except Exception as e:
            logger.exception(f"Exception captured in '{func.__name__}':{e}")
            raise
    return wrapper