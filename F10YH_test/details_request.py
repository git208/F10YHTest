import requests
import json
from ddt import data,ddt,unpack
import unittest

heads = {
    'token':'MitakeWeb',
    'Param':'-1,,100',
    'src':'d'
}
stocknews_details = []
stockbulletin_details = []
stockreport_details = []

@ddt
class test_f10YH_KN(unittest.TestCase):

    #个股新闻详情测试
    # @data("600519.sh")
    @data("600519.sh","900905.sh","689009.sh","600900.sh","600809.sh","688200.sh","511310.sh","501064.sh","511310.sh","502006.sh","502003.sh","113041.sh","204182.sh","110044.sh","019545.sh","120603.sh","300760.sz","200581.sz","002985.sz","300841.sz","300869.sz","300661.sz","000538.sz","159972.sz","160133.sz","159001.sz","184801.sz","123013.sz","131802.sz","123013.sz","101528.sz","111073.sz","600702.sh","002192.sz","430198.bj","400059.bj","820021.bj","873548.bj","830899.bj","430719.bj","873250.bj","430353.bj","835033.bj","841036.bj","430047.bj","00700.hk","03690.hk","08083.hk")
    def test04_stocknews(self,data):
        list_ID = []
        print('新闻接口，当前测试代码：',data)
        heads['Symbol'] = data
        response1 = requests.request(method="get",url='http://114.80.155.47:22013/v2/stocknewslist',headers=heads)
        for temp in response1.json()['List']:
            if 'ID' in temp.keys():
                list_ID.append(temp['ID'])
        # print(json.dumps(response1.json()['List'],indent=2,ensure_ascii=False))
        stocknews_details.append(str('-----------------'+data+'的100条新闻详情数据-----------------'))
        for id in list_ID:
            heads['Symbol'] = id
            response2 = requests.request(method="get", url='http://114.80.155.47:22013/v2/stocknews', headers=heads)
            self.assertNotEqual(response2.json(),[])
            self.assertTrue('REPORTTITLE' in response2.json().keys())
            self.assertTrue('INIPUBDATE' in response2.json().keys())
            self.assertTrue('MEDIANAME' in response2.json().keys())
            self.assertTrue('PURL' in response2.json().keys())
            self.assertTrue('ID' in response2.json().keys())
            self.assertTrue('ABSTRACT' in response2.json().keys())
            stocknews_details.append(response2.json())
        # print(json.dumps(list_xiangqing,indent=2,ensure_ascii=False))

    #个股公告详情测试
    # @data("600519.sh")
    @data("600519.sh","900905.sh","689009.sh","600900.sh","600809.sh","688200.sh","511310.sh","501064.sh","511310.sh","502006.sh","502003.sh","113041.sh","204182.sh","110044.sh","019545.sh","120603.sh","300760.sz","200581.sz","002985.sz","300841.sz","300869.sz","300661.sz","000538.sz","159972.sz","160133.sz","159001.sz","184801.sz","123013.sz","131802.sz","123013.sz","101528.sz","111073.sz","600702.sh","002192.sz","430198.bj","400059.bj","820021.bj","873548.bj","830899.bj","430719.bj","873250.bj","430353.bj","835033.bj","841036.bj","430047.bj","00700.hk","03690.hk","08083.hk")
    def test05_stockbulletinlist(self,data):
        list_ID = []
        print('公告接口，当前测试代码：',data)
        heads['Symbol'] = data
        response1 = requests.request(method="get", url='http://114.80.155.47:22013/v2/stockbulletinlist', headers=heads)
        for temp in response1.json()['List']:
            if 'ID' in temp.keys():
                list_ID.append(temp['ID'])
            # print(json.dumps(response1.json()['List'],indent=2,ensure_ascii=False))
        stockbulletin_details.append(str('-----------------' + data + '的100条新闻详情数据-----------------'))
        for id in list_ID:
            heads['Symbol'] = id
            response2 = requests.request(method="get", url='http://114.80.155.47:22013/v2/stockbulletin', headers=heads)
            self.assertNotEqual(response2.json(), [])
            self.assertTrue('DATASOUCE' in response2.json().keys())
            self.assertTrue('TITLE' in response2.json().keys())
            self.assertTrue('PURL' in response2.json().keys())
            self.assertTrue('ID' in response2.json().keys())
            self.assertTrue('CONTENT' in response2.json().keys())
            self.assertTrue('PUBDATE' in response2.json().keys())
            stockbulletin_details.append(response2.json())

    # 个股研报详情测试
    @data("600519.sh","900905.sh","689009.sh","600900.sh","600809.sh","688200.sh","300760.sz","200581.sz","002985.sz","300841.sz","300869.sz","300661.sz","000538.sz","600702.sh","002192.sz","00700.hk","03690.hk","08083.hk","430198.bj","400059.bj","820021.bj","873548.bj","830899.bj","430719.bj","873250.bj","430353.bj","835033.bj","841036.bj","430047.bj")
    def test06_stockreportlist(self,data):
        list_ID = []
        print('研报接口，当前测试代码：',data)
        heads['Symbol'] = data
        response1 = requests.request(method="get", url='http://114.80.155.47:22013/v2/stockreportlist', headers=heads)
        for temp in response1.json()['List']:
            if 'ID' in temp.keys():
                list_ID.append(temp['ID'])
            # print(json.dumps(response1.json()['List'],indent=2,ensure_ascii=False))
        stockreport_details.append(str('-----------------' + data + '的100条新闻详情数据-----------------'))
        for id in list_ID:
            heads['Symbol'] = id
            response2 = requests.request(method="get", url='http://114.80.155.47:22013/v2/stockreport', headers=heads)
            self.assertNotEqual(response2.json(), [])
            self.assertTrue('REPORTTITLE' in response2.json().keys())
            self.assertTrue('DATASOUCE' in response2.json().keys())
            self.assertTrue('PURL' in response2.json().keys())
            self.assertTrue('ID' in response2.json().keys())
            self.assertTrue('PUBDATE' in response2.json().keys())
            self.assertTrue('ABSTRACT' in response2.json().keys())
            stockreport_details.append(response2.json())
    @classmethod
    def tearDownClass(cls) -> None:
        with open(file='responses_stocknews.txt', mode='w', encoding='utf-8') as a:
            a.write(json.dumps(stocknews_details, indent=2, ensure_ascii=False))
        with open(file='responses_stockbulletin.txt', mode='w', encoding='utf-8') as a:
            a.write(json.dumps(stockbulletin_details, indent=2, ensure_ascii=False))
        with open(file='responses_stockreport.txt', mode='w', encoding='utf-8') as a:
            a.write(json.dumps(stockreport_details, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    unittest.main()
