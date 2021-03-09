import json
import os
import unittest

import HtmlTestRunner

from MyFrameTest.test_case.test_cases_form_excel import TestCaseFormExcel
from MyFrameTest.test_case.test_cases_form_yaml import TestCaseFormYaml

file= '../test_case/excels/接口.xlsx'
file_type = 'excel'
assign_case_list = []


if __name__ == '__main__':
    print('创建或更新用例列表')
    with open('../source/testCaseDriver.json', mode='w', encoding='utf-8') as a:
        if file_type.lower() == 'yaml':
            if assign_case_list == []:
                a.write(json.dumps(os.listdir('../test_case/yamls'), ensure_ascii=False,indent=2))
            else: