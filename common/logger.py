# -*- coding: gbk -*-
import logging
import datetime
import os


class Logger:

    @staticmethod
    def logger_in():
        # ������־��
        logger = logging.getLogger("APIlogger")
        logger.setLevel(logging.DEBUG)
        # �ж��Ƿ����handler����Ȼÿ�ζ����½�һ��handler��������־�ظ����
        if not logger.handlers:
            # ��ȡ��ǰ����Ϊ�ļ�����������2λ+�·�+����
            file_name = str(datetime.datetime.now().strftime('%g' + '%m' + "%d")) + '.log'
            # ����������
            handler = logging.FileHandler(os.path.join('./log', file_name))
            # handler = logging.StreamHandler()
            # ������ʽ��
            formatter = logging.Formatter('%(asctime)s [%(filename)s:%(lineno)d] %(levelname)s  %(message)s',
                                          '%Y-%m-%d %H:%M:%S')
            logger.addHandler(handler)
            handler.setFormatter(formatter)
        return logger

# if __name__ == '__main__':
#     Logger.logger_in().warning("����һ������")
