from common.logger import Logger


class Assert:
    #   实现断言，并且将断言的结果写入到日志中

    @staticmethod
    def code_assert(response, assert_type,assert_msg):
        if assert_type == "code":
            try:
                assert response.status_code == assert_msg
                Logger.logger_in().info('断言成功！')
            except Exception as e:
                Logger.logger_in().error('断言失败！原因是：{}'.format(repr(e)))
            # print(response.text)
        else:
            print("请输入code")

        if assert_type == "massage":
            try:
                assert response.text == assert_msg
                Logger.logger_in().info('断言成功！')
            except Exception as e:
                Logger.logger_in().error('断言失败！原因是：{}'.format(repr(e)))
                # print(response.text)
            else:
                print("请输入massage")



