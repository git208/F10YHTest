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

id_stocknewslist = []
id_stockbulletinlist = []
id_stockreportlist = []

fy_id_stocknewslist = []
fy_id_stockbulletinlist = []
fy_id_stockreportlist = []


@ddt
class test_PB(unittest.TestCase):
    # @data("600519.sh")
    @data("600519.sh","900905.sh","689009.sh","600900.sh","600809.sh","688200.sh","511310.sh","501064.sh","511310.sh","502006.sh","502003.sh","113041.sh","204182.sh","110044.sh","019545.sh","120603.sh","300760.sz","200581.sz","002985.sz","300841.sz","300869.sz","300661.sz","000538.sz","159972.sz","160133.sz","159001.sz","184801.sz","123013.sz","131802.sz","123013.sz","101528.sz","111073.sz","600702.sh","002192.sz","430198.bj","400059.bj","820021.bj","873548.bj","830899.bj","430719.bj","873250.bj","430353.bj","835033.bj","841036.bj","430047.bj","00700.hk","03690.hk","08083.hk")
    def test01_stocknewslist(self,data):
        print('新闻接口')
        heads['Symbol'] = data
        response = requests.request(method="get",url='http://114.80.155.47:22013/v2/stocknewslist',headers=heads)
        temp_list = []
        index = int(response.json()['Cnt']/2)
        temp_list.append(response.json()['List'][index]['ID'])
        # temp_list.append(response.json()['List'][index+1]['ID'])
        # temp_list.append(response.json()['List'][index+2]['ID'])
        try:
            _ = response.json()['List'][index]['ID']
            _ = response.json()['List'][index - 5]['ID']
        except BaseException as s:
            print('异常信息：',s)
        else:
            id_stocknewslist.append(temp_list)
            fy_id_stocknewslist.append(response.json()['List'][index-5]['ID'])
        print('Cnt =',response.json()['Cnt'])
        print(temp_list)


    # # @data("600519.sh")
    @data("600519.sh","900905.sh","689009.sh","600900.sh","600809.sh","688200.sh","511310.sh","501064.sh","511310.sh","502006.sh","502003.sh","113041.sh","204182.sh","110044.sh","019545.sh","120603.sh","300760.sz","200581.sz","002985.sz","300841.sz","300869.sz","300661.sz","000538.sz","159972.sz","160133.sz","159001.sz","184801.sz","123013.sz","131802.sz","123013.sz","101528.sz","111073.sz","600702.sh","002192.sz","430198.bj","400059.bj","820021.bj","873548.bj","830899.bj","430719.bj","873250.bj","430353.bj","835033.bj","841036.bj","430047.bj","00700.hk","03690.hk","08083.hk")
    def test02_stockbulletinlist(self,data):
        print('公告接口')
        heads['Symbol'] = data
        response = requests.request(method="get", url='http://114.80.155.47:22013/v2/stockbulletinlist', headers=heads)
        index = int(response.json()['Cnt'] / 2)
        temp_list = []
        temp_list.append(response.json()['List'][index]['ID'])
        # temp_list.append(response.json()['List'][index + 1]['ID'])
        # temp_list.append(response.json()['List'][index + 2]['ID'])
        try:
            _ = response.json()['List'][index]['ID']
            _ = response.json()['List'][index - 5]['ID']
        except BaseException as s:
            print('异常信息：',s)
        else:
            id_stockbulletinlist.append(temp_list)
            fy_id_stockbulletinlist.append(response.json()['List'][index - 5]['ID'])
        print('Cnt =', response.json()['Cnt'])
        print(temp_list)

    # @data('430353.bj','430047.bj')
    @data("600519.sh","900905.sh","689009.sh","600900.sh","600809.sh","688200.sh","300760.sz","200581.sz","002985.sz","300841.sz","300869.sz","300661.sz","000538.sz","600702.sh","002192.sz","00700.hk","03690.hk","08083.hk","430198.bj","400059.bj","820021.bj","873548.bj","830899.bj","430719.bj","873250.bj","430353.bj","835033.bj","841036.bj","430047.bj")
    def test03_stockreportlist(self,data):
        print('研报接口')
        heads['Symbol'] = data
        response = requests.request(method="get", url='http://114.80.155.47:22013/v2/stockreportlist', headers=heads)
        temp_list = []
        index = int(response.json()['Cnt'] / 2)

        temp_list.append(response.json()['List'][index]['ID'])
        # temp_list.append(response.json()['List'][index + 1]['ID'])
        # temp_list.append(response.json()['List'][index + 2]['ID'])
        try:
            _ = response.json()['List'][index]['ID']
            _ = response.json()['List'][index - 5]['ID']
        except BaseException as s:
            print('异常信息：',s)
        else:
            id_stockreportlist.append(temp_list)
            fy_id_stockreportlist.append(response.json()['List'][index - 5]['ID'])
        print('Cnt =', response.json()['Cnt'],temp_list,response.json()['List'][index - 5]['ID'])
        print('----',id_stockreportlist)
        print(temp_list)


    @classmethod
    def tearDownClass(cls) -> None:
        ret = []
        fy_ID = []
        ret.append({'新闻ID列表':id_stocknewslist})
        ret.append({'公告ID列表': id_stockbulletinlist})
        ret.append({'研报ID列表': id_stockreportlist})

        fy_ID.append({'新闻翻页ID列表': fy_id_stocknewslist})
        fy_ID.append({'公告翻页ID列表': fy_id_stockbulletinlist})
        fy_ID.append({'研报翻页ID列表': fy_id_stockreportlist})
        with open(file='any_result/PB_ID.txt', mode='w', encoding='utf-8') as a:
            a.write(json.dumps(ret, indent=2, ensure_ascii=False))
        with open(file='any_result/PB_FY_ID.txt', mode='w', encoding='utf-8') as a:
            a.write(json.dumps(fy_ID, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    unittest.main()
