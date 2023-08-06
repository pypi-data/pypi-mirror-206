import pytest

from luckyun_logger import get_logger

class TestLogger:

    def test_logger(self): 
       logger = get_logger(__name__)
       logger.debug('debug')
       logger.info('info')
