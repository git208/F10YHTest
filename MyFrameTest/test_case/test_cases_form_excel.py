import json
import os
import unittest

import HtmlTestRunner
from ddt import ddt, file_data, unpack

from ..public.file_to_case import FileToCase

file='excels/接口.xlsx'
file_type='excel'
sheet_name=None

@ddt
class TestCaseFormExcel(unittest.TestCase):

    def setUp(self) -> None:
        pass

    @file_data('../source/testCaseDriver.json')
    @unpack
    def test_01(self, case_identifier):
        print(case_identifier)
        case = FileToCase(file,file_type,case_identifier=case_identifier,sheet_name=sheet_name)
        print(case.testName, '</p><p>')
        response = case.requests()
        print(json.dumps(response.json(), ensure_ascii=False, indent=2))
        pass

    def tearDown(self) -> None:
        pass

@ddt
class TestCaseFormYaml(unittest.TestCase):

    def setUp(self) -> None:
        pass

    @file_data('../source/testCaseDriver.json')
    @unpack
    def test_01(self,yaml_file):
        case = FileToCase(file=f'../source/yamls/{yaml_file}',file_type='yaml')
        print(case.testName,'</p><p>')
        response = case.requests()
        # print(json.dumps(response.json(),ensure_ascii=False,indent=2))
        print(response.text)
        pass

    def tearDown(self) -> None:
        pass

if __name__ == '__main__':

    print(unittest.TestLoader().getTestCaseNames(TestCaseFormExcel))
    suit = unittest.TestSuite()
    for temp in unittest.TestLoader().getTestCaseNames(TestCaseFormExcel):
        suit.addTest(TestCaseFormExcel(temp))
    HtmlTestRunner.HTMLTestRunner(output='../reports/', report_title='溜冰的测试报告').run(suit)