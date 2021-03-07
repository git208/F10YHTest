import json
import os
import unittest

import HtmlTestRunner
from ddt import ddt, file_data, unpack

from MyFrameTest.public.file_to_case import FileToCase


@ddt
class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    @file_data('../source/testCaseName.json')
    @unpack
    def test_01(self,yaml_file,):
        case = FileToCase(file=f'../source/yamls/{yaml_file}',file_type='yaml')
        print(case.testName,'</p><p>')
        response = case.requests()
        print(json.dumps(response.json(),ensure_ascii=False,indent=2))
        pass

    def tearDown(self) -> None:
        pass

if __name__ == '__main__':

    print(unittest.TestLoader().getTestCaseNames(TestCase))
    suit = unittest.TestSuite()
    i = 0
    for temp in os.listdir('../source/yamls'):
        i += 1
        suit.addTest(TestCase(f'test_01_0000{i}_{temp}'.replace('.', '_')))
    HtmlTestRunner.HTMLTestRunner(output='../reports/', report_title='溜冰的测试报告').run(suit)