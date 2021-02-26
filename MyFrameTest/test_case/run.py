import json
import os,sys
import unittest

import HtmlTestRunner

from MyFrameTest.test_case.test_cases_drive import TestCase


def create_ddt_file():
    print('创建或更新用例列表')
    with open('../source/testCaseName.json', mode='w', encoding='utf-8') as a:
        a.write(
            json.dumps(os.listdir('../source/yamls'), ensure_ascii=False,
                       indent=2))

def testExecution():
    suit = unittest.TestSuite()
    i = 0
    for temp in os.listdir('../source/yamls'):
        i += 1
        suit.addTest(TestCase(f'test_01_0000{i}_{temp}'.replace('.', '_')))
    HtmlTestRunner.HTMLTestRunner(output='../reports/', report_title='溜冰的测试报告').run(suit)

if __name__ == '__main__':
    if os.path.exists('../source/testCaseName.json'):
        with open('../source/testCaseName.json', mode='r', encoding='utf-8') as a:
            if len(json.load(a)) != len(os.listdir('../source/yamls')):
                create_ddt_file()
            else:
                testExecution()
    else:
        create_ddt_file()