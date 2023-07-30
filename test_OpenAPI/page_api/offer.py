#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
from utils.read_yaml import read_yaml
from utils.requests_utils import RequestUtils


class Offer:

    # 获取offer类型id
    @staticmethod
    def get_offer_type(path, get_headers):
        data = read_yaml(path)
        # print(json.dumps(header))
        response = RequestUtils().send_request(method=data["method"], url=data["url"], data=json.dumps(data["body"]),
                                               headers=get_headers)
        # print(response.request.body)
        response = json.loads(response.text)
        # print(data['data'][0]["dataSourceResults"][0]["value"])
        # return data['data'][0]["dataSourceResults"][0]["value"]
        return response
    # 创建offer
    @staticmethod
    def create_offer(data, headers, get_offer_type, get_applicant_id, get_apply_id):
        # print(data)
        # print(data["json"])
        # body = json.dumps(data["json"])
        # json.loads(body)
        # 将json的值从字符串转换成字典类型
        body = eval(data["json"])
        body["offerTypeID"] = get_offer_type
        body["applicantId"] = get_applicant_id
        body["applyId"] = get_apply_id
        response = RequestUtils().send_request(url=data["url"], method=data["method"],
                                               json=body, headers=headers)
        response = json.loads(response.text)
        return response

    # 根据offerid查询offer
    @staticmethod
    def get_offer(path, header, offer_id):
        data = read_yaml(path)
        offer_id = str(offer_id)
        body = [offer_id]
        response = RequestUtils().send_request(url=data['url'], method=data["method"], json=body, headers=header)
        return response
