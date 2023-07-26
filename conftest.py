# -*- coding: gbk -*-
import pytest

from common.logger import Logger
from utils.read_yaml import read_yaml
from utils.requests_utils import RequestUtils


@pytest.fixture(scope="class")
def get_headers():
    try:
        # 读取获取token需要用到的数据
        data_token = read_yaml("./get_token.yml")
        # 获取token
        response = RequestUtils().send_request(url=data_token["url"], method=data_token["method"],
                                               json=data_token["json"])

        token_value = response.json()["access_token"]
        Logger.logger_in().info('token获取成功，token值为：{}'.format(token_value))
        headers = {
            "Authorization": "Bearer" + ' ' + token_value,
            "Host": "openapi.italent.cn",
            "Content-Type": "application/json"
        }

        return headers
    except Exception as e:
        # print(repr(e))
        Logger.logger_in().error('获取token失败，原因为{}'.format(repr(e)))


if __name__ == '__main__':
    get_headers()
