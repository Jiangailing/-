import openpyxl


# 读取测试数据方法封装
class ExcelHandler:
    def __init__(self, path):
        self.path = path

    def open_excel(self, sheet_name):
        #  读取excel文件
        wb = openpyxl.load_workbook(self.path)
        # 获取sheet
        sheet = wb[sheet_name]
        wb.close()
        return sheet

    def get_header(self, sheet_name):
        # 获取表头
        sheet = self.open_excel(sheet_name)
        header = []
        # 遍历第一行，获取表头
        for i in sheet[1]:
            header_value = i.value
            header.append(header_value)
        return header

    def read_excel(self, sheet_name):
        sheet = self.open_excel(sheet_name)  # 获取sheet
        rows = list(sheet.rows)  # 将sheet里面的每一行转换成列表，方便进行遍历
        data = []
        for row in rows[1:]:
            row_data = []
            for cell in row:
                row_data.append(cell.value)
            data_dict = dict(zip(self.get_header(sheet_name), row_data))
            # print(data_dict)  # 将每一行的值与表头关联起来
            data.append(data_dict)

        return data

    @staticmethod
    def write_excel(file, sheet_name, row, cloumn, data):
        # excel写入数据
        wb = openpyxl.load_workbook(file)
        sheet = wb[sheet_name]
        sheet.cell[row, cloumn].value = data
        wb.save(file)
        wb.close()
#
# if __name__ == '__main__':
#     excel = ExcelHandler("../test_Beisenopenapi/data/createoffer.xlsx")
#     data = excel.read_excel("Sheet1")
#     print(data)
