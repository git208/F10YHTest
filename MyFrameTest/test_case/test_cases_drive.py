import json
import os
import unittest

import HtmlTestRunner
import requests
from ddt import ddt, file_data, unpack

from MyFrameTest.public.file_to_case import FileToCase


@ddt
class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    # @file_data('../source/testCaseName.json')
    # @unpack
    # def test_01(self,yaml_file):
    #     case = FileToCase(file=f'../source/yamls/{yaml_file}',file_type='yaml')
    #     print(case.testName,'</p><p>')
    #     response = case.requests()
    #     # print(json.dumps(response.json(),ensure_ascii=False,indent=2))
    #     print(response.text)
    #     pass

    @file_data('../source/testCaseName.json')
    @unpack
    def test_01(self, file):
        print(file)
        case = FileToCase(file='../source/excels/接口.xlsx', file_type='excel',case_number=file)
        print(case.testName, '</p><p>')
        response = case.requests()
        print(json.dumps(response.json(), ensure_ascii=False, indent=2))
        pass

    def tearDown(self) -> None:
        pass

if __name__ == '__main__':

    print(unittest.TestLoader().getTestCaseNames(TestCase))
    suit = unittest.TestSuite()
    for temp in unittest.TestLoader().getTestCaseNames(TestCase):
        suit.addTest(TestCase(temp))
    HtmlTestRunner.HTMLTestRunner(output='../reports/', report_title='溜冰的测试报告').run(suit)