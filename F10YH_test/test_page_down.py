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

    # @data(("600519.sh", "600519.sh_20180606020006537823_20180606"),("900905.sh", "900905.sh_20200803020011822288_20200803"),
    #       ("689009.sh", "689009.sh_20200427020011199163_20200427"),("600900.sh", "600900.sh_20190513020008390299_20190513"),
    #       ("600809.sh", "600809.sh_20190305020007925950_20190305"),("511310.sh", "511310.sh_20181120020007180411_20181120"),
    #       ("501064.sh", "501064.sh_20190107020007484272_20190107"),("511310.sh", "511310.sh_20190121020007562327_20190121"),
    #       ("502006.sh", "502006.sh_20180723020006688490_20180723"),("502003.sh", "502003.sh_20181016020006975704_20181016"),
    #       ("113041.sh", "113041.sh_20181211030000828950_20181211"),("110044.sh", "110044.sh_20190830020009257770_20190830"),
    #       ("019545.sh", "019545.sh_20170602020005331729_20170602"),("120603.sh", "120603.sh_20181107020007095731_20181107"),
    #       ("300760.sz", "300760.sz_20190710020008839628_20190227"),("300841.sz", "300841.sz_20200805020011841500_20200805"),
    #       ("300661.sz", "300661.sz_20191222020010261463_20191222"),("000538.sz", "000538.sz_20181023020007013208_20181023"),
    #       ("159972.sz", "159972.sz_20181018020006986375_20181017"),("160133.sz", "160133.sz_20180808020006744763_20180808"),
    #       ("159001.sz", "159001.sz_20180607020006541006_20180607"),("184801.sz", "184801.sz_20190226020007840873_20190226"),
    #       ("123013.sz", "123013.sz_20210121020012986436_20210121"),("101528.sz", "101528.sz_20170523020005306484_20170523"),
    #       ("111073.sz", "111073.sz_20190517020008415270_20190517"),("600702.sh", "600702.sh_20190220020007770800_20190220"),
    #       ("002192.sz", "002192.sz_20190520020008428788_20190520"),("830899.bj", "830899.bj_20190410020008203429_20190410"),
    #       ("430719.bj", "430719.bj_20180207020006169820_20180207"),("00700.hk", "00700.hk_20180307020006234172_20180307"),
    #       ("03690.hk", "03690.hk_20181018020006988120_20181018"))
    # @data(("600000.sh", "600000.sh_20210203020013065183"))
    # @unpack
    # def test01_stocknewslist(self,code,ID):
    #     print('新闻接口，当前测试参数：',code,ID)
    #     heads['Symbol'] = code
    #     responseAll = requests.request(method="get", url='http://114.80.155.47:22013/v2/stocknewslist', headers=heads)
    #     for temp in responseAll.json()['List']:
    #         dict_data[temp['ID']] = temp
    #         list_data.append(temp['ID'])
    #     heads['Param'] = ID + ',300'
    #     response300 = requests.request(method="get", url='http://114.80.155.47:22013/v2/stocknewslist', headers=heads)
    #
    #     self.assertEqual(str(response300.json()['Cnt']),'300')
    #     self.assertEqual(response300.json()['List'][0]['ID'],
    #                      responseAll.json()['List'][list_data.index(ID) + 1]['ID'])
    #     for temp in response300.json()['List']:
    #         self.assertEqual(temp['REPORTTITLE'], dict_data[temp['ID']]['REPORTTITLE'])
    #         self.assertEqual(temp['ISPDF'], dict_data[temp['ID']]['ISPDF'])
    #         self.assertEqual(temp['INIPUBDATE'], dict_data[temp['ID']]['INIPUBDATE'])
    #         self.assertEqual(temp['MEDIANAME'], dict_data[temp['ID']]['MEDIANAME'])
    #         self.assertEqual(temp['STOCKNAME'], dict_data[temp['ID']]['STOCKNAME'])
    #         self.assertEqual(temp['ID'], dict_data[temp['ID']]['ID'])
    #         self.assertEqual(temp['ENTRYDATE'], dict_data[temp['ID']]['ENTRYDATE'])
    #         self.assertEqual(temp['ENTRYTIME'], dict_data[temp['ID']]['ENTRYTIME'])

        # print(json.dumps(response.json(),ensure_ascii=False,indent=2))



    # @data(("600900.sh","600900.sh_5613952_20190830"),("019545.sh","019545.sh_6012695_20170818"),
    #       ("120603.sh","120603.sh_7886898_20180514"),("300841.sz","300841.sz_6859434_20210119"),
    #       ("300661.sz","300661.sz_5643794_20190911"),("000538.sz","000538.sz_5370163_20190516"),
    #       ("101528.sz","101528.sz_6001132_20170817"),("600702.sh","600702.sh_5061466_20190302"),
    #       ("002192.sz","002192.sz_5390504_20190522"))
    # @data(('600000.sh','600000.sh_6721166'))
    # @unpack
    # def test02_stockbulletinlist(self,code,ID):
    #     print('公告接口，当前测试参数：', code, ID)
    #     heads['Symbol'] = code
    #     responseAll = requests.request(method="get", url='http://114.80.155.47:22013/v2/stockbulletinlist', headers=heads)
    #     for temp in responseAll.json()['List']:
    #         dict_data[temp['ID']] = temp
    #         list_data.append(temp['ID'])
    #     heads['Param'] = ID + ',300'
    #     response300 = requests.request(method="get", url='http://114.80.155.47:22013/v2/stockbulletinlist', headers=heads)
    #
    #     self.assertEqual(str(response300.json()['Cnt']), '300')
    #     self.assertEqual(response300.json()['List'][0]['ID'],
    #                      responseAll.json()['List'][list_data.index(ID) + 1]['ID'])
    #     for temp in response300.json()['List']:
    #         self.assertEqual(temp['ISPDF'], dict_data[temp['ID']]['ISPDF'])
    #         self.assertEqual(temp['DATASOUCE'], dict_data[temp['ID']]['DATASOUCE'])
    #         self.assertEqual(temp['STOCKNAME'], dict_data[temp['ID']]['STOCKNAME'])
    #         self.assertEqual(temp['TITLE'], dict_data[temp['ID']]['TITLE'])
    #         self.assertEqual(temp['ID'], dict_data[temp['ID']]['ID'])
    #         self.assertEqual(temp['PUBDATE'], dict_data[temp['ID']]['PUBDATE'])
    #         self.assertEqual(temp['ENTRYDATE'], dict_data[temp['ID']]['ENTRYDATE'])
    #         self.assertEqual(temp['ENTRYTIME'], dict_data[temp['ID']]['ENTRYTIME'])


    # @data(("00700.hk","00700.hk_5045039_20200722"))
    @data(('600000.sh','600000.sh_5206609'))
    @unpack
    def test03_stockreportlist(self,code,ID):
        print('研报接口，当前测试参数：', code, ID)
        heads['Symbol'] = code
        responseAll = requests.request(method="get", url='http://114.80.155.47:22013/v2/stockreportlist',headers=heads)
        for temp in responseAll.json()['List']:
            dict_data[temp['ID']] = temp
            list_data.append(temp['ID'])
        heads['Param'] = ID + ',300'
        response300 = requests.request(method="get", url='http://114.80.155.47:22013/v2/stockreportlist',headers=heads)

        self.assertEqual(str(response300.json()['Cnt']), '300')
        self.assertEqual(response300.json()['List'][0]['ID'],
                         responseAll.json()['List'][list_data.index(ID) + 1]['ID'])
        for temp in response300.json()['List']:
            self.assertEqual(temp['REPORTTITLE'], dict_data[temp['ID']]['REPORTTITLE'])
            self.assertEqual(temp['ISPDF'], dict_data[temp['ID']]['ISPDF'])
            self.assertEqual(temp['DATASOUCE'], dict_data[temp['ID']]['DATASOUCE'])
            self.assertEqual(temp['STOCKNAME'], dict_data[temp['ID']]['STOCKNAME'])
            self.assertEqual(temp['ID'], dict_data[temp['ID']]['ID'])
            self.assertEqual(temp['PUBDATE'], dict_data[temp['ID']]['PUBDATE'])
            self.assertEqual(temp['ENTRYDATE'], dict_data[temp['ID']]['ENTRYDATE'])
            self.assertEqual(temp['ENTRYTIME'], dict_data[temp['ID']]['ENTRYTIME'])



if __name__ == '__main__':
    unittest.main()
