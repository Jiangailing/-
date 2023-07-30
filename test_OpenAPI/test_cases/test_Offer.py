#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import os
import allure
import pytest
from common.get_data import GetData
from common.wrappers import write_case_log
from common.assert_cases import Assert
from test_OpenAPI.page_api.applicants import Applicant
from test_OpenAPI.page_api.applys import Apply
from test_OpenAPI.page_api.offer import Offer
from utils.requests_utils import RequestUtils


def get_data():
    return GetData.get_data(os.path.basename(__file__))


class TestOffer:
    """未分对象做封装前的实现"""

    # @pytest.fixture()
    # def get_offertype(self,get_headers):
    #     data = read_yaml("./get_type.yml")
    #     # print(json.dumps(header))
    #     response = RequestUtils().send_request(method="post", url=data["url"], data=json.dumps(data["body"]),
    #                                            headers=get_headers)
    #     print(response.request.body)
    #     data = json.loads(response.text)
    #     print(data['data'][0]["dataSourceResults"][0]["value"])
    #     return data['data'][0]["dataSourceResults"][0]["value"]
    #
    # @pytest.fixture()
    # def get_applicant(self,get_headers):
    #     data = read_yaml("./get_applicant.yml")
    #     print(json.dumps(data))
    #     response = RequestUtils().send_request(method="post", url=data["url"], data=json.dumps(data["body"]),
    #                                            headers=get_headers)
    #     print(response.text)
    #     data = json.loads(response.text)
    #     return data['data'][0]
    #
    # @pytest.fixture()
    # def get_applyid(self, get_applicant, get_headers):
    #     data = read_yaml("./get_applyid.yml")
    #     print(data)
    #     applicant_id = str(get_applicant)
    #     data["body"] = {
    #         'applicantIds': [applicant_id]
    #     }
    #     body = data["body"]
    #     print(type(body))
    #     print(data)
    #     response = RequestUtils().send_request(method="post", url=data["url"],
    #                                            data=json.dumps(body, default=str, ensure_ascii=False),
    #                                            headers=get_headers)
    #     print(response.request.body)
    #     data = json.loads(response.text)
    #     print(data['data'][0]['applyId'])
    #     return data['data'][0]['applyId']
    #
    # @write_case_log
    # @allure.title("{data[title]}")  # 命名用例名称方式1
    # @allure.severity(allure.severity_level.CRITICAL)
    # @pytest.mark.parametrize("data", get_data())
    # def test_create_offer(self, data, get_headers, get_offertype, get_applicant, get_applyid):
    #     # print(data)
    #     # print(data["json"])
    #     # body = json.dumps(data["json"])
    #     # json.loads(body)
    #     body = eval(data["json"])
    #     body["offerTypeID"] = get_offertype
    #     body["applicantId"] = get_applicant
    #     body["applyId"] = get_applyid
    #     response = RequestUtils().send_request(url=data["url"], method=data["method"],
    #                                            json=body, headers=get_headers)
    #     print(response.text)
    #     Assert.code_assert(response, "code", data["code"])

    # 按对象封装接口请求后的用例，测试生成offer，传入应聘者id、申请id以及offer类型id
    @write_case_log
    @allure.title("{data[title]}")  # 命名用例名称方式1
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("data", get_data())
    def test_create_offer(self, data, get_headers):
        applicant_id = Applicant.get_applicant_id('./data/get_applicant.yml', get_headers)
        create_offer_response = Offer.create_offer(data, get_headers,
                                                   Offer.get_offer_type('./data/get_type.yml', get_headers)['data'][0]["dataSourceResults"][0]["value"],
                                                   applicant_id,
                                                   Apply.get_apply_id('./data/get_applyid.yml', applicant_id,
                                                                      get_headers))
        # print(response.text)
        response = Offer.get_offer('./data/get_offer.yml', get_headers, create_offer_response["data"])
        # print(response)
        response = json.loads(response.text)
        # 若能根据新建的offer的offerid能查询到对应的offer，那么说明新建offer成功
        Assert.custom_assert(create_offer_response["data"], response["data"][0]["id"])
# if __name__ == '__main__':
#     t = Testopenapi
#     t.test_create_offer()
