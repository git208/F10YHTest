import json
import unittest

from ddt import ddt, file_data, unpack

from MyFrameTest.public.yaml.yaml_to_case import YamlToCase


@ddt
class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    @file_data('../source/testCaseName.json')
    @unpack
    def test_01(self,yaml_file):
        case = YamlToCase(f'../source/yamls/{yaml_file}')
        print(case.testName,'</p><p>')
        response = case.requests()
        print(json.dumps(response.json(),ensure_ascii=False,indent=2))
        pass

    def tearDown(self) -> None:
        pass




    # print(unittest.TestLoader().getTestCaseNames(TestCase))