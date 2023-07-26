# -*- coding: gbk -*-
import logging
import datetime
import os


class Logger:

    @staticmethod
    def logger_in():
        # 创建日志器
        logger = logging.getLogger("APIlogger")
        logger.setLevel(logging.DEBUG)
        # 判断是否存在handler，不然每次都会新建一个handler，导致日志重复输出
        if not logger.handlers:
            # 获取当前日期为文件名，年份最后2位+月份+日期
            file_name = str(datetime.datetime.now().strftime('%g' + '%m' + "%d")) + '.log'
            # 创建处理器
            handler = logging.FileHandler(os.path.join('./log', file_name))
            # handler = logging.StreamHandler()
            # 创建格式器
            formatter = logging.Formatter('%(asctime)s [%(filename)s:%(lineno)d] %(levelname)s  %(message)s',
                                          '%Y-%m-%d %H:%M:%S')
            logger.addHandler(handler)
            handler.setFormatter(formatter)
        return logger

# if __name__ == '__main__':
#     Logger.logger_in().warning("这是一个错误")
