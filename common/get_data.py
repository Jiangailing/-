# -*- coding: gbk -*-
import os
import re

from utils.excel_handle import ExcelHandler


class GetData:
    # 通过filename传入参数，通过使用正则表达式，截取出filename中_后的关键字，使用os.path.join()方法将路径和文件名拼接在一起，
    # 封装一个静态方法，方便在每个用例处调用，减少不必要的内存占用和性能消耗

    @staticmethod
    def get_data(filename):
        data_names = re.findall(r'_(.*?)\.', filename)
        data_name = str(data_names[0]) + '.xlsx'
        path = os.path.join('./data/test_data/', data_name)
        excel_cases = ExcelHandler(path)
        data_cases = excel_cases.read_excel("Sheet1")
        print(data_cases)
        return data_cases
