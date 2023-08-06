# log_helper.py

import logging
import logging.handlers
import logging.config
import time
import os


class CustomTimedRotatingFileHandler(logging.handlers.TimedRotatingFileHandler):
    def __init__(self, filename, when='h', interval=1, backupCount=0, encoding=None, delay=False, utc=False, atTime=None):
        current_time = time.strftime("%Y-%m-%d", time.localtime())
        filename = filename.replace('%Y', current_time[:4]).replace(
            '%m', current_time[5:7]).replace('%d', current_time[8:10])
        super().__init__(filename, when, interval, backupCount, encoding, delay, utc, atTime)


log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'defaultFormatter': {
            'format': log_format,
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'consoleHandler': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'defaultFormatter',
            'stream': 'ext://sys.stdout',
        },
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['consoleHandler']
        },
    }
}

logs_folder = 'logs'
if not os.path.exists(logs_folder):
    os.mkdir(logs_folder)

log_file = os.path.join(logs_folder, 'app-%Y-%m-%d.log')

file_handler = CustomTimedRotatingFileHandler(
    log_file, when='midnight', interval=1, backupCount=7)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter(
    log_format))

logging.config.dictConfig(LOGGING_CONFIG)


def get_logger(name=None):
    logger = logging.getLogger(name)
    logger.addHandler(file_handler)
    return logger
