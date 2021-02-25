import json
import time
import _thread
from ddt import ddt,data,file_data,unpack
from MyFrameTest.common.yaml_to_case import YamlToCase
import unittest
import HtmlTestRunner
import os


def create_ddt_file(self):
    with open('../source/testCaseName.json', mode='w', encoding='utf-8') as a:
        a.write(
            json.dumps(os.listdir('/Users/far/Desktop/自动化/F10YHTest/MyFrameTest/yamls'), ensure_ascii=False,
                       indent=2))


def testExecution():
    suit = unittest.TestSuite()
    time.sleep(5)
    i = 0
    for temp in os.listdir('/Users/far/Desktop/自动化/F10YHTest/MyFrameTest/yamls'):
        i += 1
        suit.addTest(TestCase(f'test_01_0000{i}_{temp}'.replace('.', '_')))
    HtmlTestRunner.HTMLTestRunner(output='../reports/', report_title='溜冰的测试报告').run(suit)

@ddt
class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    @file_data('../source/testCaseName.json')
    @unpack
    def test_01(self,yaml_file):
        case = YamlToCase(f'../yamls/{yaml_file}')
        print(case.testName)
        response = case.requests()
        print(json.dumps(response.json(),ensure_ascii=False,indent=2))
        pass

    def tearDown(self) -> None:
        pass

if __name__ == '__main__':

    _thread.start_new_thread(create_ddt_file,('生成数据驱动文件中',20))
    if os.path.exists('/Users/far/Desktop/自动化/F10YHTest/MyFrameTest/source/testCaseName.json'):
        _thread.exit_thread()
        testExecution()
    while(1):
        pass
    # unittest.main()
    # print(unittest.TestLoader().getTestCaseNames(TestCase))


    # suit.addTest(TestCase('test_01_00001_stockbulletinlist_yaml'))
    # unittest.TextTestRunner().run(suit)
