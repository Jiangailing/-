# -*- coding: gbk -*-
from common.logger import Logger


class Assert:
    #   ʵ�ֶ��ԣ����ҽ����ԵĽ��д�뵽��־��

    @staticmethod
    def code_assert(response, assert_type,assert_msg):
        if assert_type == "code":
            try:
                assert response.status_code == assert_msg
                Logger.logger_in().info('���Գɹ���')
            except Exception as e:
                Logger.logger_in().error('����ʧ�ܣ�ԭ���ǣ�{}'.format(repr(e)))
            # print(response.text)
        else:
            print("������code")

        if assert_type == "massage":
            try:
                assert response.text == assert_msg
                Logger.logger_in().info('���Գɹ���')
            except Exception as e:
                Logger.logger_in().error('����ʧ�ܣ�ԭ���ǣ�{}'.format(repr(e)))
                # print(response.text)
            else:
                print("������massage")



