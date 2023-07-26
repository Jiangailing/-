import requests

from common.logger import Logger
from utils.read_yaml import get_baseurl


# 统一接口请求封装
class RequestUtils:
    session = requests.session()

    def __init__(self):
        self.get_url = get_baseurl("./base_url.yml", "base", "url")  # 读取不同环境的url，方便切换测试环境和线上环境

    def send_request(self, url, method, **kwargs):
        try:
            url_1 = self.get_url + url
            # print(self.get_url)
            # print(url_1)
            response = RequestUtils.session.request(url=url_1, method=method, **kwargs)
            Logger.logger_in().info('接口请求成功，响应值为：{}'.format(response.text))
            return response
        except Exception as e:
            Logger.logger_in().error('接口请求失败，原因为：{}'.format(repr(e)))

# if __name__ == '__main__':
#     url=RequestUtils()
#     url.send_request("123")
