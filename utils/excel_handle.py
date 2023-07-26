import openpyxl


# ��ȡ�������ݷ�����װ
class ExcelHandler:
    def __init__(self, path):
        self.path = path

    def open_excel(self, sheet_name):
        #  ��ȡexcel�ļ�
        wb = openpyxl.load_workbook(self.path)
        # ��ȡsheet
        sheet = wb[sheet_name]
        wb.close()
        return sheet

    def get_header(self, sheet_name):
        # ��ȡ��ͷ
        sheet = self.open_excel(sheet_name)
        header = []
        # ������һ�У���ȡ��ͷ
        for i in sheet[1]:
            header_value = i.value
            header.append(header_value)
        return header

    def read_excel(self, sheet_name):
        sheet = self.open_excel(sheet_name)  # ��ȡsheet
        rows = list(sheet.rows)  # ��sheet�����ÿһ��ת�����б�������б���
        data = []
        for row in rows[1:]:
            row_data = []
            for cell in row:
                row_data.append(cell.value)
            data_dict = dict(zip(self.get_header(sheet_name), row_data))
            # print(data_dict)  # ��ÿһ�е�ֵ���ͷ��������
            data.append(data_dict)

        return data

    @staticmethod
    def write_excel(file, sheet_name, row, cloumn, data):
        # excelд������
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
