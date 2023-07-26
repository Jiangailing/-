import json
import os
import allure
import pytest
from common.get_data import GetData
from common.wrappers import write_case_log
from common.assert_cases import Assert
from utils.requests_utils import RequestUtils


def get_data():
    return GetData.get_data(os.path.basename(__file__))


class TestOffer:

    @write_case_log
    @allure.title("{data[title]}")  # 命名用例名称方式1
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("data", get_data())
    def test_create_offer(self, data, get_headers):
        response1 = RequestUtils().send_request(url=data["url"], method=data["method"],
                                                json=json.loads(data["json"]), headers=get_headers)
        print(response1.text)
        Assert.code_assert(response1, "code", data["code"])

# if __name__ == '__main__':
#     t = Testopenapi
#     t.test_create_offer()
