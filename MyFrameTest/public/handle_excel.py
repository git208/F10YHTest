import openpyxl
import json
import time

import requests
class HandleExcel:

    def __init__(self, filename, sheetname=None, caseNumber=0):
        self.filename = filename
        self.sheetname = sheetname
        self.data = self.get_excel()[caseNumber]

    def get_excel(self):
        """
        获取excel中的用例
        :return:
        """
        wb = openpyxl.load_workbook(self.filename)
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
        if key in self.data['teststeps']['request'].keys():
            if self.data['teststeps']['request'][key] == "":
                return None
            else:
                return self.data['teststeps']['request'][key]
        else:
            return None

    def get_testName(self):
        if 'name' in self.data['config'].keys():
            if self.data['config']['name'] == "":
                return None
            else:
                return self.data['config']['name']
        else:
            return None

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
    das = HandleExcel('../source/excels/接口.xlsx')

    print(das.get_excel())

