# -*- coding: gbk -*-
from common.logger import Logger


class Assert:
    #   实现断言，并且将断言的结果写入到日志中
    @staticmethod
    def custom_assert(response_assert,assert_msg):
        try:
            assert response_assert == assert_msg
            Logger.logger_in().info('断言成功！')
        except Exception as e:
            Logger.logger_in().error('断言失败！原因是：{}'.format(repr(e)))



