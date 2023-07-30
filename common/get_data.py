# -*- coding: gbk -*-
import os
import re

from utils.excel_handle import ExcelHandler


class GetData:
    # ͨ��filename���������ͨ��ʹ��������ʽ����ȡ��filename��_��Ĺؼ��֣�ʹ��os.path.join()������·�����ļ���ƴ����һ��
    # ��װһ����̬������������ÿ�����������ã����ٲ���Ҫ���ڴ�ռ�ú���������

    @staticmethod
    def get_data(filename):
        data_names = re.findall(r'_(.*?)\.', filename)
        data_name = str(data_names[0]) + '.xlsx'
        path = os.path.join('./data/test_data/', data_name)
        excel_cases = ExcelHandler(path)
        data_cases = excel_cases.read_excel("Sheet1")
        print(data_cases)
        return data_cases
