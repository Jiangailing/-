from functools import wraps

from common.logger import Logger


def write_case_log(func):
    """
    ��¼����������־
    :param func:
    :return:
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        Logger.logger_in().info('{}��ʼִ��'.format(func.__name__))
        func(*args, **kwargs)
        Logger.logger_in().info('{}ִ�����'.format(func.__name__))
    return wrapper

