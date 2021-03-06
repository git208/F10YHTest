import unittest

import requests
from ddt import ddt, data, file_data, unpack

heads = {
    'token':'MitakeWeb',
    'src':'d'
}
ID_list_x = []
ID_list_g = []
ID_list_y = []
@ddt
class PBFYTest(unittest.TestCase):
    def setUp(self) -> None:
        pass
    @data(("430198.bj","430198.bj_6008505_20200408","430198.bj_5962148_20200324"),
            ("400059.bj","400059.bj_5625114_20190830","400059.bj_5522010_20190801"),
            ("820021.bj","820021.bj_5594424_20190826","820021.bj_5594409_20190826"),
            ("873548.bj","873548.bj_6754175_20201130","873548.bj_6751173_20201127"),
            ("830899.bj","830899.bj_5729997_20191104","830899.bj_5635883_20190906"),
            ("430719.bj","430719.bj_5103172_20190321","430719.bj_4959072_20181227"),
            ("873250.bj","873250.bj_5929963_20200310","873250.bj_5912798_20200228"),
            ("430353.bj","430353.bj_5514442_20190729","430353.bj_5470955_20190702"),
            ("835033.bj","835033.bj_6247473_20200430","835033.bj_6245928_20200430"),
            ("430047.bj","430047.bj_6375619_20200617","430047.bj_6341763_20200602"),
            ("00700.hk","00700.hk_1428719_20190729","00700.hk_1410503_20190606"),
            ("03690.hk","03690.hk_1445274_20190905","03690.hk_1434064_20190809"),
            ("08083.hk","08083.hk_1428149_20190726","08083.hk_1400218_20190521"))
    @unpack
    def test01_xinwen(self,code, ID,PBID):
        print('公告接口，当前测试参数：',code,ID)
        heads['Symbol'] = code
        heads['Param'] = ID + ',300'
        response = requests.request(method="get", url='http://114.80.155.47:22013/v2/stockbulletinlist', headers=heads)
        # print(response.json())
        for temp in response.json()['List']:
            ID_list_x.append(temp['ID'])
        # print(ID_list_x)
        self.assertIn(PBID, ID_list_x)

    @data(("600519.sh","600519.sh_4611114_20190812","600519.sh_4580837_20190722"),
            ("689009.sh","689009.sh_5155299_20201012","689009.sh_5286605_20210113"),
            ("600900.sh","600900.sh_4703548_20191025","600900.sh_4673654_20190924"),
            ("600809.sh","600809.sh_4705001_20191028","600809.sh_4704235_20191027"),
            ("688200.sh","688200.sh_5173762_20201026","688200.sh_5064470_20200806"),
            ("300760.sz","300760.sz_4717886_20191104","300760.sz_4712240_20191030"),
            ("002985.sz","002985.sz_5217793_20201123","002985.sz_5168475_20201021"),
            ("300841.sz","300841.sz_5204833_20201111","300841.sz_5134741_20200918"),
            ("300661.sz","300661.sz_4712719_20191031","300661.sz_4708973_20191029"),
            ("000538.sz","000538.sz_4634928_20190826","000538.sz_4490429_20190507"),
            ("600702.sh","600702.sh_4233191_20181026","600702.sh_4162607_20180822"),
            ("00700.hk","00700.hk_4617794_20190815","00700.hk_4591028_20190729"),
            ("03690.hk","03690.hk_4843253_20200225","03690.hk_4815262_20200204"),
            ("08083.hk","08083.hk_5070820_20200811","08083.hk_4916300_20200414"),
            ("430198.bj","430198.bj_5044020_20200721","430198.bj_5164993_20201020"))
    @unpack
    def test02_gonggao(self, code, ID, PBID):
        print('研报接口，当前测试参数：', code, ID)
        heads['Symbol'] = code
        heads['Param'] = ID + ',300'
        response = requests.request(method="get", url='http://114.80.155.47:22013/v2/stockreportlist', headers=heads)
        # print(response.json())
        for temp in response.json()['List']:
            ID_list_x.append(temp['ID'])
        print(ID_list_x)
        self.assertIn(PBID, ID_list_x)

    def tearDown(self) -> None:
        pass

if __name__ == '__main__':
    unittest.main()