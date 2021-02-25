import json
import unittest

from ddt import data, ddt, unpack, file_data

from F10YH_test.file_format import xinWengFomat,gongGaoFomat,yanbaoFomat



@ddt
class contrastHistory(unittest.TestCase):

    def test01_contrast_stocknewslist(self):
        # print(json.dumps(xinWengFomat(), indent=2, ensure_ascii=False),'\n---------------------------\n---------------------------')
        print('新闻：---------------------------\n---------------------------')
        dic_base = xinWengFomat()
        with open(file='any_result/responses_stocknewslist.txt', mode='r', encoding='utf-8') as b:
            dic_Interface = json.loads(b.read())
            for key in dic_base.keys():
                # print('当前判断ID：', key)
                if key in dic_Interface.keys():
                    try:
                        self.assertIn(dic_base[key]['INIPUBDATE'], dic_Interface[key]['INIPUBDATE'])
                        # self.assertIn(dic_base[key]['ENTRYDATE'], dic_Interface[key]['ENTRYDATE'])
                        # self.assertEqual(dic_Interface[key]['ENTRYTIME'], dic_base[key]['ENTRYTIME'])
                        self.assertEqual(dic_Interface[key]['REPORTTITLE'], dic_base[key]['REPORTTITLE'])
                        self.assertEqual(dic_Interface[key]['ISPDF'], dic_base[key]['ISPDF'])
                    except AssertionError as e:
                        print('断言异常：\n',dic_Interface[key]['ID'],'\n',e)
                else:
                    print('未找到的ID：', key,dic_base[key]['INIPUBDATE'])

    def test02_contrast_stockbulletinlist(self):
        # print(json.dumps(gongGaoFomat(), indent=2, ensure_ascii=False),
        #       '\n---------------------------\n---------------------------')
        print('公告：---------------------------\n---------------------------')
        dic_base = gongGaoFomat()
        with open(file='any_result/responses_stockbulletinlist.txt', mode='r', encoding='utf-8') as b:
            dic_Interface = json.loads(b.read())
            for key in dic_base.keys():
                # print('当前判断ID：', key)
                if key in dic_Interface.keys():
                    try:
                        self.assertEqual(dic_Interface[key]['PUBDATE'], dic_base[key]['PUBDATE'])
                        # self.assertEqual(dic_Interface[key]['ENTRYDATE'], dic_base[key]['ENTRYDATE'])
                        # self.assertEqual(dic_Interface[key]['ENTRYTIME'], dic_base[key]['ENTRYTIME'])
                        self.assertEqual(dic_Interface[key]['TITLE'], dic_base[key]['TITLE'])
                        self.assertEqual(dic_Interface[key]['DATASOUCE'], dic_base[key]['DATASOUCE'])
                        self.assertEqual(dic_Interface[key]['STOCKNAME'], dic_base[key]['STOCKNAME'])
                        self.assertEqual(dic_Interface[key]['ISPDF'], dic_base[key]['ISPDF'])
                    except AssertionError as e:
                        print('断言异常：\n', dic_Interface[key]['ID'], '\n', e)
                else:
                    print('未找到的ID：', key,dic_base[key]['PUBDATE'])

    def test03_contrast_stockreportlist(self):
        # print(json.dumps(yanbaoFomat(), indent=2, ensure_ascii=False),
        #       '\n---------------------------\n---------------------------')
        print('研报：---------------------------\n---------------------------')
        dic_base = yanbaoFomat()
        with open(file='any_result/responses_stockreportlist.txt', mode='r', encoding='utf-8') as b:
            dic_Interface = json.loads(b.read())
            for key in dic_base.keys():
                # print('当前判断ID：', key)
                if key in dic_Interface.keys():
                    try:
                        self.assertEqual(dic_Interface[key]['PUBDATE'], dic_base[key]['PUBDATE'])
                        # self.assertEqual(dic_Interface[key]['ENTRYDATE'], dic_base[key]['ENTRYDATE'])
                        # self.assertEqual(dic_Interface[key]['ENTRYTIME'], dic_base[key]['ENTRYTIME'])
                        self.assertEqual(dic_Interface[key]['REPORTTITLE'], dic_base[key]['REPORTTITLE'])
                        self.assertEqual(dic_Interface[key]['DATASOUCE'], dic_base[key]['DATASOUCE'])
                        self.assertEqual(dic_Interface[key]['STOCKNAME'], dic_base[key]['STOCKNAME'])
                        self.assertEqual(dic_Interface[key]['ISPDF'], dic_base[key]['ISPDF'])
                    except AssertionError as e:
                        print('断言异常：\n', dic_Interface[key]['ID'], '\n', e)
                else:
                    print('未找到的ID：', key,dic_base[key]['PUBDATE'])




if __name__ == '__main__':
    unittest.main()
