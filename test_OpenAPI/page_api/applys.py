# -*- coding: gbk -*-
import json
from utils.read_yaml import read_yaml
from utils.requests_utils import RequestUtils


class Apply:

    # 获取应聘者申请id
    @staticmethod
    def get_apply_id(path, applicant_id, get_headers):
        data = read_yaml(path)
        # print(data)
        applicant_id = str(applicant_id)
        data["body"] = {
            'applicantIds': [applicant_id]
        }
        body = data["body"]
        # print(type(body))
        # print(data)
        response = RequestUtils().send_request(method=data["method"], url=data["url"],
                                               data=json.dumps(body, default=str, ensure_ascii=False),
                                               headers=get_headers)
        # print(response.request.body)
        response = json.loads(response.text)
        # print(data['data'][0]['applyId'])
        # return data['data'][0]['applyId']
        return response
