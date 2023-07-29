#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import os
from ast import literal_eval

import allure
import pytest
from common.get_data import GetData
from common.wrappers import write_case_log
from common.assert_cases import Assert
from utils.read_yaml import read_yaml
from utils.requests_utils import RequestUtils


def get_data():
    return GetData.get_data(os.path.basename(__file__))


class TestOffer:

    @pytest.fixture()
    def get_offertype(self,get_headers):
        data = read_yaml("./get_type.yml")
        # print(json.dumps(header))
        response = RequestUtils().send_request(method="post", url=data["url"], data=json.dumps(data["body"]),
                                               headers=get_headers)
        print(response.request.body)
        data = json.loads(response.text)
        print(data['data'][0]["dataSourceResults"][0]["value"])
        return data['data'][0]["dataSourceResults"][0]["value"]

    @pytest.fixture()
    def get_applicant(self,get_headers):
        data = read_yaml("./get_applicant.yml")
        print(json.dumps(data))
        response = RequestUtils().send_request(method="post", url=data["url"], data=json.dumps(data["body"]),
                                               headers=get_headers)
        print(response.text)
        data = json.loads(response.text)
        return data['data'][0]

    @pytest.fixture()
    def get_applyid(self, get_applicant, get_headers):
        data = read_yaml("./get_applyid.yml")
        print(data)
        applicant_id = str(get_applicant)
        data["body"] = {
            'applicantIds': [applicant_id]
        }
        body = data["body"]
        print(type(body))
        print(data)
        response = RequestUtils().send_request(method="post", url=data["url"],
                                               data=json.dumps(body, default=str, ensure_ascii=False),
                                               headers=get_headers)
        print(response.request.body)
        data = json.loads(response.text)
        print(data['data'][0]['applyId'])
        return data['data'][0]['applyId']

    @write_case_log
    @allure.title("{data[title]}")  # 命名用例名称方式1
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("data", get_data())
    def test_create_offer(self, data, get_headers, get_offertype, get_applicant, get_applyid):
        # print(data)
        # print(data["json"])
        # body = json.dumps(data["json"])
        # json.loads(body)
        body = eval(data["json"])
        body["offerTypeID"] = get_offertype
        body["applicantId"] = get_applicant
        body["applyId"] = get_applyid
        response = RequestUtils().send_request(url=data["url"], method=data["method"],
                                               json=body, headers=get_headers)
        print(response.text)
        Assert.code_assert(response, "code", data["code"])
# if __name__ == '__main__':
#     t = Testopenapi
#     t.test_create_offer()
