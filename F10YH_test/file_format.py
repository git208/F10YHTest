import json

class fileFormatTXT():
    def delete(self,list):
        listtemp = []
        list.remove(list[0])
        for temp in list :
            listtemp.append(temp.replace('\n','').split('	'))
        return listtemp

    # 新闻字段
    def SH_SZ_BJ_fomat(self,list):
        dic = {}
        for temp1 in list:
            if temp1 != []:
                dic[temp1[0]] = {
                    'INIPUBDATE':temp1[1],
                    'ENTRYDATE':temp1[2],
                    'ENTRYTIME':temp1[3],
                    'REPORTTITLE':temp1[4],
                    # 'DATASOUCE': temp1[8],
                    # 'STOCKNAME': temp1[6],
                    'ISPDF':temp1[6]
                    }
        return dic

    # 新闻字段
    def HK_fomat(self,list):
        dic = {}
        for temp1 in list:
            if temp1 != []:
                dic[temp1[3]] = {
                    'INIPUBDATE':temp1[4],
                    'ENTRYDATE':temp1[5],
                    'ENTRYTIME':temp1[6],
                    'REPORTTITLE':temp1[8],
                    # 'DATASOUCE': temp1[7],
                    # 'STOCKNAME': temp1[9],
                    'ISPDF':temp1[11]
                }
        return dic

    # 新闻字段
    def JJ_ZQ_fomat(self,list):
        dic = {}
        for temp1 in list:
            if temp1 != []:
                dic[temp1[2]] = {
                    'INIPUBDATE':temp1[3],
                    'ENTRYDATE':temp1[4],
                    'ENTRYTIME':temp1[5],
                    'REPORTTITLE':temp1[7],
                    # 'DATASOUCE': temp1[6],
                    # 'STOCKNAME': temp1[8],
                    'ISPDF':temp1[10]
                }
        return dic

    # 公告字段
    def GG_BJ_fomat(self, list):
        dic = {}
        for temp1 in list:
            if temp1 != []:
                dic[temp1[1]] = {
                    'PUBDATE': temp1[2].replace(' ',''),
                    'ENTRYDATE': temp1[4],
                    'ENTRYTIME': temp1[5],
                    'TITLE': temp1[3],
                    'DATASOUCE': temp1[8],
                    'STOCKNAME': temp1[6].replace(' ',''),
                    'ISPDF': temp1[7]
                }
        return dic

class fileFormatSQL():
    def delete(self,list):
        listtemp = []
        for temp in list :
            if '|' in temp and 'ID' not in temp:
                listtemp.append(str(temp).replace(" ","").split('|'))
        return listtemp

    #公告字段
    def SH_SZ_fomat(self,list):
        dic = {}
        for temp1 in list:
            if temp1 != []:
                dic[temp1[2]] = {
                    'PUBDATE':temp1[3],
                    'ENTRYDATE':temp1[5],
                    'ENTRYTIME':temp1[6],
                    'TITLE':temp1[4],
                    'DATASOUCE':temp1[9],
                    'STOCKNAME':temp1[7],
                    'ISPDF':temp1[8]
                }
        return dic

    # 公告字段
    def HK_fomat(self,list):
        dic = {}
        for temp1 in list:
            if temp1 != []:
                dic[temp1[1]] = {
                    'PUBDATE':temp1[4],
                    'ENTRYDATE':temp1[9],
                    'ENTRYTIME':temp1[10],
                    'TITLE':temp1[5],
                    'DATASOUCE':temp1[8],
                    'STOCKNAME':temp1[6],
                    'ISPDF':temp1[7]
                }
        return dic

    # 公告字段
    def JJ_fomat(self,list):
        dic = {}
        for temp1 in list:
            if temp1 != []:
                dic[temp1[1]] = {
                    'PUBDATE':temp1[3],
                    'ENTRYDATE':temp1[8],
                    'ENTRYTIME':temp1[9],
                    'TITLE':temp1[4],
                    'DATASOUCE':temp1[7],
                    'STOCKNAME':temp1[5],
                    'ISPDF':temp1[6]
                }
        return dic

    # 公告字段
    def ZQ_fomat(self,list):
        dic = {}
        for temp1 in list:
            if temp1 != []:
                dic[temp1[2]] = {
                    'PUBDATE':temp1[3],
                    'ENTRYDATE':temp1[8],
                    'ENTRYTIME':temp1[9],
                    'TITLE':temp1[4],
                    'DATASOUCE':temp1[7],
                    'STOCKNAME':temp1[5],
                    'ISPDF':temp1[6]
                }
        return dic

    # 研报字段
    def YB_SH_SZ_HK_BJ_fomat(self, list):
        dic = {}
        for temp1 in list:
            if temp1 != []:
                dic[temp1[2]] = {
                    'PUBDATE': temp1[3],
                    'ENTRYDATE': temp1[4],
                    'ENTRYTIME': temp1[5],
                    'REPORTTITLE': temp1[6],
                    'DATASOUCE': temp1[8],
                    'STOCKNAME': temp1[7],
                    'ISPDF': temp1[10]
                }
        return dic

def xinWengFomat():
    dic_merge = {}
    self = fileFormatTXT()
    with open(file='source/01sql/bnd_news_2017.txt', mode='r', encoding='utf-8') as a:
        temp = self.JJ_ZQ_fomat(self.delete(a.readlines()))
        dic_merge.update(temp)
    with open(file='source/01sql/bnd_news_2018.txt', mode='r', encoding='utf-8') as a:
        temp = self.JJ_ZQ_fomat(self.delete(a.readlines()))
        dic_merge.update(temp)
    with open(file='source/01sql/bnd_news_2019.txt', mode='r', encoding='utf-8') as a:
        temp = self.JJ_ZQ_fomat(self.delete(a.readlines()))
        dic_merge.update(temp)
    with open(file='source/01sql/bnd_news_2020.txt', mode='r', encoding='utf-8') as a:
        temp = self.JJ_ZQ_fomat(self.delete(a.readlines()))
        dic_merge.update(temp)
    with open(file='source/01sql/fnd_news_2017.txt', mode='r', encoding='utf-8') as a:
        temp = self.JJ_ZQ_fomat(self.delete(a.readlines()))
        dic_merge.update(temp)
    with open(file='source/01sql/fnd_news_2018.txt', mode='r', encoding='utf-8') as a:
        temp = self.JJ_ZQ_fomat(self.delete(a.readlines()))
        dic_merge.update(temp)
    with open(file='source/01sql/fnd_news_2019.txt', mode='r', encoding='utf-8') as a:
        temp = self.JJ_ZQ_fomat(self.delete(a.readlines()))
        dic_merge.update(temp)
    with open(file='source/01sql/fnd_news_2020.txt', mode='r', encoding='utf-8') as a:
        temp = self.JJ_ZQ_fomat(self.delete(a.readlines()))
        dic_merge.update(temp)
    with open(file='source/01sql/hk_news_2017.txt', mode='r', encoding='utf-8') as a:
        temp = self.HK_fomat(self.delete(a.readlines()))
        dic_merge.update(temp)
    with open(file='source/01sql/hk_news_2018.txt', mode='r', encoding='utf-8') as a:
        temp = self.HK_fomat(self.delete(a.readlines()))
        dic_merge.update(temp)
    with open(file='source/01sql/hk_news_2019.txt', mode='r', encoding='utf-8') as a:
        temp = self.HK_fomat(self.delete(a.readlines()))
        dic_merge.update(temp)
    with open(file='source/01sql/hk_news_2020.txt', mode='r', encoding='utf-8') as a:
        temp = self.HK_fomat(self.delete(a.readlines()))
        dic_merge.update(temp)
    with open(file='source/01sql/sk_news_2017.txt', mode='r', encoding='utf-8') as a:
        temp = self.SH_SZ_BJ_fomat(self.delete(a.readlines()))
        dic_merge.update(temp)
    with open(file='source/01sql/sk_news_2018.txt', mode='r', encoding='utf-8') as a:
        temp = self.SH_SZ_BJ_fomat(self.delete(a.readlines()))
        dic_merge.update(temp)
    with open(file='source/01sql/sk_news_2019.txt', mode='r', encoding='utf-8') as a:
        temp = self.SH_SZ_BJ_fomat(self.delete(a.readlines()))
        dic_merge.update(temp)
    with open(file='source/02sql/bj_news_2017.txt', mode='r', encoding='utf-8') as a:
        temp = self.SH_SZ_BJ_fomat(self.delete(a.readlines()))
        dic_merge.update(temp)
    with open(file='source/02sql/bj_news_2018.txt', mode='r', encoding='utf-8') as a:
        temp = self.SH_SZ_BJ_fomat(self.delete(a.readlines()))
        dic_merge.update(temp)
    with open(file='source/02sql/bj_news_2019.txt', mode='r', encoding='utf-8') as a:
        temp = self.SH_SZ_BJ_fomat(self.delete(a.readlines()))
        dic_merge.update(temp)
    with open(file='source/02sql/bj_news_2021.txt', mode='r', encoding='utf-8') as a:
        temp = self.SH_SZ_BJ_fomat(self.delete(a.readlines()))
        dic_merge.update(temp)
    # print(json.dumps(dic_merge, indent=2, ensure_ascii=False))
    return dic_merge


def gongGaoFomat():
    format_SQL = fileFormatSQL()
    format_TXT = fileFormatTXT()
    dic_merge = {}
    with open(file='source/stock_bulletin.sql', mode='r', encoding='utf-8') as a:
        lists = a.readlines()
        list_SH_SZ = lists[0:lists.index('-- 公告港股\n')]
        list_HK = lists[lists.index('-- 公告港股\n'):lists.index('--  公告基金\n')]
        list_JJ = lists[lists.index('--  公告基金\n'):lists.index('-- 债券\n')]
        list_ZQ = lists[lists.index('-- 债券\n'):]
        dic_merge.update(format_SQL.SH_SZ_fomat(format_SQL.delete(list_SH_SZ)))
        dic_merge.update(format_SQL.HK_fomat(format_SQL.delete(list_HK)))
        dic_merge.update(format_SQL.JJ_fomat(format_SQL.delete(list_JJ)))
        dic_merge.update(format_SQL.ZQ_fomat(format_SQL.delete(list_ZQ)))
    with open(file='source/02sql/bj_bulletin_2017.txt', mode='r', encoding='utf-8') as a:
        temp = format_TXT.GG_BJ_fomat(format_TXT.delete(a.readlines()))
        dic_merge.update(temp)
    with open(file='source/02sql/bj_bulletin_2018.txt', mode='r', encoding='utf-8') as a:
        temp = format_TXT.GG_BJ_fomat(format_TXT.delete(a.readlines()))
        dic_merge.update(temp)
    with open(file='source/02sql/bj_bulletin_2019.txt', mode='r', encoding='utf-8') as a:
        temp = format_TXT.GG_BJ_fomat(format_TXT.delete(a.readlines()))
        dic_merge.update(temp)
    with open(file='source/02sql/bj_bulletin_2020.txt', mode='r', encoding='utf-8') as a:
        temp = format_TXT.GG_BJ_fomat(format_TXT.delete(a.readlines()))
        dic_merge.update(temp)
    # print(json.dumps(dic_merge, indent=2, ensure_ascii=False))
    return dic_merge

def yanbaoFomat():
    format_SQL = fileFormatSQL()
    dic_merge = {}
    with open(file='source/stock_report.sql', mode='r', encoding='utf-8') as a:
        lists = a.readlines()
        list_SH_SZ = lists[0:lists.index('--  研报 港股\n')]
        list_HK = lists[lists.index('--  研报 港股\n'):lists.index('--  研报 新三板\n')]
        list_BJ = lists[lists.index('--  研报 新三板\n'):]
        dic_merge.update(format_SQL.YB_SH_SZ_HK_BJ_fomat(format_SQL.delete(list_SH_SZ)))
        dic_merge.update(format_SQL.YB_SH_SZ_HK_BJ_fomat(format_SQL.delete(list_HK)))
        dic_merge.update(format_SQL.YB_SH_SZ_HK_BJ_fomat(format_SQL.delete(list_BJ)))
        # print(json.dumps(dic_merge, indent=2, ensure_ascii=False))
    return dic_merge

if __name__ == '__main__':
    print(json.dumps(yanbaoFomat(), indent=2, ensure_ascii=False))