# -*- coding: gbk -*-
import pytest

from common.logger import Logger
from utils.read_yaml import read_yaml
from utils.requests_utils import RequestUtils


@pytest.fixture(scope="class")
def get_headers():
    try:
        # ��ȡ��ȡtoken��Ҫ�õ�������
        data_token = read_yaml("./get_token.yml")
        # ��ȡtoken
        response = RequestUtils().send_request(url=data_token["url"], method=data_token["method"],
                                               json=data_token["json"])

        token_value = response.json()["access_token"]
        Logger.logger_in().info('token��ȡ�ɹ���tokenֵΪ��{}'.format(token_value))
        headers = {
            "Authorization": "Bearer" + ' ' + token_value,
            "Host": "openapi.italent.cn",
            "Content-Type": "application/json"
        }

        return headers
    except Exception as e:
        # print(repr(e))
        Logger.logger_in().error('��ȡtokenʧ�ܣ�ԭ��Ϊ{}'.format(repr(e)))


if __name__ == '__main__':
    get_headers()
