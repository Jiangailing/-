# -*- coding: gbk -*-
from common.logger import Logger


class Assert:
    #   ʵ�ֶ��ԣ����ҽ����ԵĽ��д�뵽��־��
    @staticmethod
    def custom_assert(response_assert,assert_msg):
        try:
            assert response_assert == assert_msg
            Logger.logger_in().info('���Գɹ���')
        except Exception as e:
            Logger.logger_in().error('����ʧ�ܣ�ԭ���ǣ�{}'.format(repr(e)))



