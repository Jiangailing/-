from functools import wraps

from common.logger import Logger


def write_case_log(func):
    """
    记录用例运行日志
    :param func:
    :return:
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        Logger.logger_in().info('{}开始执行'.format(func.__name__))
        func(*args, **kwargs)
        Logger.logger_in().info('{}执行完毕'.format(func.__name__))
    return wrapper

