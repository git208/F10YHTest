import openpyxl
import json
import time

import requests
class HandleExcel:

    def __init__(self, file, sheet_name=None, case_number=0):
        self.filepath = file
        self.sheetname = sheet_name
        self.data = self.get_excel()[case_number-1]

    def get_excel(self):
        """
        获取excel中的用例
        :return:
        """
        wb = openpyxl.load_workbook(self.filepath)
        if self.sheetname is None:
            ws = wb.active
        else:
            ws = wb[self.sheetname]
        head_tuple = tuple(ws.iter_rows(max_row=1, values_only=True))[0]
        print(head_tuple)
        one_list = []
        for other_tuple in tuple(ws.iter_rows(min_row=2, values_only=True)):
            one_list.append(dict(zip(head_tuple, other_tuple)))
        return one_list

    def data_process(self, key):
        if key in self.data.keys():
            if self.data[key] == "":
                return None
            else:
                return self.data[key]
        else:
            return None

    def get_testName(self):
        return self.data_process('title')

    def get_url(self):
        return self.data_process('url')

    def get_method(self):
        return self.data_process('method')

    def get_type(self):
        return self.data_process('type')

    def get_headers(self):
        return self.data_process('headers')

    def get_params(self):
        return self.data_process('params')

    def get_body(self):
        return self.data_process('body')


if __name__ == '__main__':
    # pass
    das = HandleExcel('../source/excels/接口.xlsx',caseNumber=1)

    print(das.get_headers())

