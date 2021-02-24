import requests
import json
from ddt import data,ddt,unpack
import unittest
import os

heads = {
    'token':'MitakeWeb',
    'src':'d'
}
dict_data = {}
list_data = []


@ddt
class test_f10YH_elapsed(unittest.TestCase):

    def setUp(self) -> None:
        heads['Param'] = '-1,,100000'
    @data(("600000.sh", "600000.sh_20210203020013065183"))
    @unpack
    def test01_stocknewslist(self,code,ID):
        print('新闻接口，当前测试参数：',code,ID)
        heads['Symbol'] = code
        responseAll = requests.request(method="get", url='http://114.80.155.57:22013/v2/stocknewslist', headers=heads)
        print(responseAll.headers)

        '''向前翻页'''
        heads['Param'] = '-1,'+ID+',100'
        print('zhengque', heads['Param'])
        print(json.dumps(list_data,ensure_ascii=False,indent=2))
        response300 = requests.request(method="get", url='http://114.80.155.57:22013/v2/stocknewslist', headers=heads)
        print(json.dumps(response300.json(),ensure_ascii=False,indent=2))
        '''向前翻页'''

        heads['Param'] = '-1,' + ID + ',100'
        print('cuowu',heads['Param'])
        response3001 = requests.request(method="get", url='http://114.80.155.57:22013/v2/stocknewslist', headers=heads)
        print(json.dumps(response3001.json(), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    unittest.main()
