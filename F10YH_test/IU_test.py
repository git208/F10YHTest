import json

import requests
import selenium
from ddt import ddt,data
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

heads = {
    'token':'MitakeWeb',
    'Param':'-1,,100000',
    'src':'d'
}
dic_stocknewslist = []
dic_stockbulletinlist = []
dic_stockreportlist = []
# driver = webdriver.Chrome(executable_path='chromedriver')
# driver.get('https://www.baidu.com')
# driver.close()
# driver.find_element(By.XPATH,'')

@ddt
class Mytest(unittest.TestCase):

    @data("600519.sh","900905.sh","689009.sh","501064.sh","113041.sh","300760.sz","200581.sz","002985.sz","159972.sz","123013.sz","430198.bj","400059.bj","873250.bj","835033.bj","00700.hk","873548.bj")
    def test_01(self,data):
        print('新闻接口')
        heads['Symbol'] = data
        response = requests.request(method="get", url='http://114.80.155.47:22013/v2/stocknewslist', headers=heads)
        dic_stocknewslist.append(response.json())
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))

    @data("600519.sh","900905.sh","689009.sh","501064.sh","113041.sh","300760.sz","200581.sz","002985.sz","159972.sz","123013.sz","430198.bj","400059.bj","873250.bj","835033.bj","00700.hk","873548.bj")
    def test_02(self,data):
        print('公告接口')
        heads['Symbol'] = data
        response = requests.request(method="get", url='http://114.80.155.47:22013/v2/stockbulletinlist', headers=heads)
        dic_stocknewslist.append(response.json())
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))

    @data("600519.sh","900905.sh","689009.sh","501064.sh","113041.sh","300760.sz","200581.sz","002985.sz","159972.sz","123013.sz","430198.bj","400059.bj","873250.bj","835033.bj","00700.hk","873548.bj")
    def test_03(self,data):
        print('研报接口')
        heads['Symbol'] = data
        response = requests.request(method="get", url='http://114.80.155.47:22013/v2/stockreportlist', headers=heads)
        dic_stocknewslist.append(response.json())
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))

    @classmethod
    def tearDownClass(cls) -> None:
        with open('./any_result/IU.txt',mode='w',encoding='utf-8') as a:
            a.write(json.dumps(dic_stocknewslist, indent=2, ensure_ascii=False))
            a.write(json.dumps(dic_stockbulletinlist, indent=2, ensure_ascii=False))
            a.write(json.dumps(dic_stockreportlist, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    unittest.main()
    print('main函数')
    pass

