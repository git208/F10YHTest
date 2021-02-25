import yaml
import requests
import json
from MyFrameTest.common.yaml_analysis import YamlAnalysis


class YamlToCase():
    def __init__(self,yaml_file):
        jsonData = YamlAnalysis(yaml_file).readYaml()
        self.testName = jsonData['config']['name']
        self.method = jsonData['teststeps']['request']['method']
        self.url = jsonData['teststeps']['request']['url']
        self.headers = jsonData['teststeps']['request']['headers']
        if self.method == 'get' or self.method == 'GET':
            self.params = jsonData['teststeps']['request']['params']
        if self.method == 'post':
            if 'json' in jsonData['teststeps']['request'].keys():
                self.json = jsonData['teststeps']['request']['json']
            if 'data' in jsonData['teststeps']['request'].keys():
                self.data = jsonData['teststeps']['request']['data']
    def requests(self):
        if self.method == 'get' or self.method == 'GET':
            response = requests.get(url=self.url,params=self.params,headers=self.headers)
        elif self.method == 'post' or self.method == 'POST' and self.json:
            response = requests.post(url=self.url,json=self.json,headers=self.headers)
        elif self.method == 'post' or self.method == 'POST' and self.data:
            response = requests.post(url=self.url,json=self.data,headers=self.headers)
        else:
            response = 'method Wrong !'
        return response


if __name__ == '__main__':
    print(YamlToCase('../yamls/stockbulletinlist.yaml').requests())