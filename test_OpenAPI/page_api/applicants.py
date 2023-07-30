#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
from utils.read_yaml import read_yaml
from utils.requests_utils import RequestUtils


class Applicant:

    # 获取应聘者id
    @staticmethod
    def get_applicant_id(path, get_headers):
        data = read_yaml(path)
        # print(json.dumps(data))
        print(data)
        response = RequestUtils().send_request(method=data["method"], url=data["url"], data=json.dumps(data["body"]),
                                               headers=get_headers)
        # print(response.text)
        data = json.loads(response.text)
        return data['data'][0]
