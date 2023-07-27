# -*- coding: gbk -*-
import logging
import datetime
import os


class Logger:
    __logger = None

    @classmethod
    def logger_in(cls):
        if cls.__logger is None:
            # 创建日志器
            cls.__logger = logging.getLogger("APIlogger")
            cls.__logger.setLevel(logging.DEBUG)
        # 判断是否存在handler，不然每次都会新建一个handler，导致日志重复输出
        if not cls.__logger.handlers:
            # 获取当前日期为文件名，年份最后2位+月份+日期
            file_name = str(datetime.datetime.now().strftime('%g' + '%m' + "%d")) + '.log'
            # 创建处理器
            handler = logging.FileHandler(os.path.join('./log', file_name))
            # handler = logging.StreamHandler()
            # 创建格式器
            formatter = logging.Formatter('%(asctime)s [%(filename)s:%(lineno)d] %(levelname)s  %(message)s',
                                          '%Y-%m-%d %H:%M:%S')
            cls.__logger.addHandler(handler)
            handler.setFormatter(formatter)
        return cls.__logger

# if __name__ == '__main__':
#     Logger.logger_in().warning("这是一个错误")
