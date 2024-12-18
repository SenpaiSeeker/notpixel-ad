import sys
from loguru import logger


logger.remove()
log_format = "<white>{time:YYYY-MM-DD HH:mm:ss}</white> | <level>{level: <8}</level> | <cyan><b>{line}</b></cyan> - <white><b>{message}</b></white>"
logger.add(sink=sys.stdout, format=log_format)
logger = logger.opt(colors=True)


def info(text):
    return logger.info(text)


def debug(text):
    return logger.debug(text)


def warning(text):
    return logger.warning(text)


def error(text):
    return logger.error(text)


def critical(text):
    return logger.critical(text)


def success(text):
    return logger.success(text)
