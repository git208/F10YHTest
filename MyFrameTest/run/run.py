import json
import os,sys
import unittest

import HtmlTestRunner

from MyFrameTest.test_case.test_cases_form_excel import TestCaseFormYaml,TestCaseFormExcel


def create_ddt_file():
    print('创建或更新用例列表')
    with open('../source/testCaseDriver.json', mode='w', encoding='utf-8') as a:
        a.write(
            json.dumps(os.listdir('../test_case/yamls'), ensure_ascii=False,
                       indent=2))

def testExecution():
    suit = unittest.TestSuite()
    for temp in unittest.TestLoader().getTestCaseNames(TestCaseFormExcel):
        suit.addTest(TestCaseFormExcel(temp))
    HtmlTestRunner.HTMLTestRunner(output='../reports/', report_title='溜冰的测试报告').run(suit)

if __name__ == '__main__':
    if os.path.exists('../source/testCaseDriver.json'):
        with open('../source/testCaseDriver.json', mode='r', encoding='utf-8') as a:
            if len(json.load(a)) != len(os.listdir('../test_case/yamls')):
                create_ddt_file()
            else:
                testExecution()
    else:
        create_ddt_file()