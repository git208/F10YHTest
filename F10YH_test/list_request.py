import requests
import json
from ddt import data,ddt,unpack
import unittest
import os

heads = {
    'token':'MitakeWeb',
    'Param':'-1,,100000',
    'src':'d'
}
dic_stocknewslist = {}
dic_stockbulletinlist = {}
dic_stockreportlist = {}


@ddt
class test_f10YH_KN(unittest.TestCase):

    # @data("600519.sh")
    @data("600519.sh","900905.sh","689009.sh","600900.sh","600809.sh","688200.sh","511310.sh","501064.sh","511310.sh","502006.sh","502003.sh","113041.sh","204182.sh","110044.sh","019545.sh","120603.sh","300760.sz","200581.sz","002985.sz","300841.sz","300869.sz","300661.sz","000538.sz","159972.sz","160133.sz","159001.sz","184801.sz","123013.sz","131802.sz","123013.sz","101528.sz","111073.sz","600702.sh","002192.sz","430198.bj","400059.bj","820021.bj","873548.bj","830899.bj","430719.bj","873250.bj","430353.bj","835033.bj","841036.bj","430047.bj","00700.hk","03690.hk","08083.hk")
    def test01_stocknewslist(self,data):
        print('新闻接口')
        heads['Symbol'] = data
        response = requests.request(method="get",url='http://114.80.155.47:22013/v2/stocknewslist',headers=heads)
        dataDict = {}
        for temp in response.json()['List']:
            if(temp != {}):
                dataDict[temp['ID'][:-9]] = temp
        dic_stocknewslist.update(dataDict)
        print(json.dumps(response.json(),indent=2,ensure_ascii=False))

    # @data("600519.sh")
    @data("600519.sh","900905.sh","689009.sh","600900.sh","600809.sh","688200.sh","511310.sh","501064.sh","511310.sh","502006.sh","502003.sh","113041.sh","204182.sh","110044.sh","019545.sh","120603.sh","300760.sz","200581.sz","002985.sz","300841.sz","300869.sz","300661.sz","000538.sz","159972.sz","160133.sz","159001.sz","184801.sz","123013.sz","131802.sz","123013.sz","101528.sz","111073.sz","600702.sh","002192.sz","430198.bj","400059.bj","820021.bj","873548.bj","830899.bj","430719.bj","873250.bj","430353.bj","835033.bj","841036.bj","430047.bj","00700.hk","03690.hk","08083.hk")
    def test02_stockbulletinlist(self,data):
        print('公告接口')
        heads['Symbol'] = data
        response = requests.request(method="get", url='http://114.80.155.47:22013/v2/stockbulletinlist', headers=heads)
        dataDict = {}
        for temp in response.json()['List']:
            if (temp != {}):
                dataDict[temp['ID'][:-9]] = json.loads(json.dumps(temp).replace(' ',''))
        dic_stockbulletinlist.update(dataDict)
        print(json.dumps(dataDict, indent=2, ensure_ascii=False))


    @data("600519.sh","900905.sh","689009.sh","600900.sh","600809.sh","688200.sh","300760.sz","200581.sz","002985.sz","300841.sz","300869.sz","300661.sz","000538.sz","600702.sh","002192.sz","00700.hk","03690.hk","08083.hk","430198.bj","400059.bj","820021.bj","873548.bj","830899.bj","430719.bj","873250.bj","430353.bj","835033.bj","841036.bj","430047.bj")
    def test03_stockreportlist(self,data):
        print('研报接口')
        heads['Symbol'] = data
        response = requests.request(method="get", url='http://114.80.155.47:22013/v2/stockreportlist', headers=heads)
        dataDict = {}
        for temp in response.json()['List']:
            if (temp != {}):
                dataDict[temp['ID'][:-9]] = json.loads(json.dumps(temp).replace(' ',''))
        dic_stockreportlist.update(dataDict)
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))

    @classmethod
    def tearDownClass(cls) -> None:
        if dic_stocknewslist != {}:
            with open(file='any_result/responses_stocknewslist.txt', mode='w', encoding='utf-8') as a:
                a.write(json.dumps(dic_stocknewslist, indent=2, ensure_ascii=False))
        if dic_stockbulletinlist != {}:
            with open(file='any_result/responses_stockbulletinlist.txt', mode='w', encoding='utf-8') as a:
                a.write(json.dumps(dic_stockbulletinlist, indent=2, ensure_ascii=False))
        if dic_stockreportlist != {}:
            with open(file='any_result/responses_stockreportlist.txt', mode='w', encoding='utf-8') as a:
                a.write(json.dumps(dic_stockreportlist, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    unittest.main()
