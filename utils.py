# -*- coding:utf-8 -*-
import sys
import os
import logging
import functools
import time


CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0



class Logger(object):
    def __init__(self, log_name, logger_name=None):
        '''
        function: log the msg to log_name file .
        args:
            log_name: log file to write
            logger_name: None,use the current file name
        '''
        if logger_name is None:
            # use file name as logger name
            logger_name = sys._getframe().f_code.co_filename
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.INFO)
        fh = logging.FileHandler(log_name)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s [%(funcName)s: %(filename)s,%(lineno)d] %(message)s")

        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

    def get_logger(self):
        return self.logger


def new_logger(log_name, logger_name=None):
    return Logger(log_name, logger_name).get_logger()


def func_info(func):
    @functools.wraps(func)
    def _deco(*args, **kwargs):
        file_name = sys._getframe().f_code.co_filename #当前文件名
        line_no = sys._getframe().f_lineno #当前行号
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print ("%s %s %s %s : enter" % (date, file_name, func.__name__, line_no))
        ret = func(*args, **kwargs)
        print ("%s %s %s %s : ret[%s] out " % (date, file_name, func.__name__, line_no, ret))
        return ret
    return _deco

@func_info
def test():
    pass

# sys._getframe().f_back.f_back.f_code.co_name,
#


if __name__ == "__main__":
    test()