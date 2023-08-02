# -*- coding: gbk -*-
import requests

from common.logger import Logger
from utils.read_yaml import get_baseurl


# ͳһ�ӿ������װ
class RequestUtils:
    session = requests.session()

    def __init__(self):
        self.get_url = get_baseurl("./base_url.yml", "base", "url")  # ��ȡ��ͬ������url�������л����Ի��������ϻ���

    def send_request(self, url, method, **kwargs):
        try:
            url_1 = self.get_url + url
            # print(self.get_url)
            # print(url_1)
            Logger.logger_in().info('-----------------{}�ӿڿ�ʼִ��-----------------'.format(url))
            response = RequestUtils.session.request(url=url_1, method=method, **kwargs)
            Logger.logger_in().info('�ӿ�����ɹ�����ӦֵΪ��{}'.format(response.text))
            return response
        except Exception as e:
            Logger.logger_in().error('�ӿ�����ʧ�ܣ�ԭ��Ϊ��{}'.format(repr(e)))
            return e


# if __name__ == '__main__':
#     url = RequestUtils()
#     url.send_request("123")
