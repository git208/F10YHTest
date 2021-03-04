import requests
from MyFrameTest.public.yaml.parse_yaml import ParseYaml
from MyFrameTest.public.request_common import form_data_format_body,form_data_format_header
from MyFrameTest.config.logConfig import LogCustom,logging

class YamlToCase():
    def __init__(self,yaml_file):
        self.handle = ParseYaml(yaml_file)
        self.testName = self.handle.get_testName()
        self.url = self.handle.get_url()
        self.method = self.handle.get_method().lower() if self.handle.get_method() != None else None
        self.type = self.handle.get_type().lower() if self.handle.get_type() != None else None
        self.headers = self.handle.get_headers()
        self.params = self.handle.get_params()
        self.body = self.handle.get_body()

    def requests(self):
        if self.method == 'get':
            response = requests.request(method='get',url=self.url,headers=self.headers,params=self.params)
        elif self.method == 'post':
            if self.type == 'form-data':
                if self.headers == None:
                    headers = form_data_format_header()
                else:
                    headers = self.headers.update(form_data_format_header())
                body = form_data_format_body(self.body)
                response = requests.request(method='post',url=self.url,headers=headers,data=body)
            elif self.type == 'x-www-form-urlencoded':
                headers = {'Content-Type':'application/x-www-form-urlencoded'}
                if self.headers == None:
                    headers = headers
                else:
                    headers = self.headers.update(headers)
                response = requests.request(method='post', url=self.url, headers=headers, data=self.body)
            elif self.type == 'json':
                headers = {'Content-Type': 'application/json'}
                if self.headers == None:
                    headers = headers
                else:
                    headers = self.headers.update(headers)
                response = requests.request(method='post', url=self.url, headers=headers, json=self.body)
            elif self.type == 'text':
                headers = {'Content-Type': 'text/plain'}
                if self.headers == None:
                    headers = headers
                else:
                    headers = self.headers.update(headers)
                response = requests.request(method='post', url=self.url, headers=headers, json=self.body)
            elif self.type == 'javascript':
                headers = {'Content-Type': 'application/javascript'}
                if self.headers == None:
                    headers = headers
                else:
                    headers = self.headers.update(headers)
                response = requests.request(method='post', url=self.url, headers=headers, json=self.body)
            elif self.type == 'html':
                headers = {'Content-Type': 'text/html'}
                if self.headers == None:
                    headers = headers
                else:
                    headers = self.headers.update(headers)
                response = requests.request(method='post', url=self.url, headers=headers, json=self.body)
            elif self.type == 'xml':
                headers = {'Content-Type': 'application/xml'}
                if self.headers == None:
                    headers = headers
                else:
                    headers = self.headers.update(headers)
                response = requests.request(method='post', url=self.url, headers=headers, json=self.body)
            else:
                LogCustom().logger().info(f'用例[{self.testName}]请求内容类型有误，请检查用例')
                response = None
        else:
            LogCustom().logger().info(f'用例[{self.testName}]请求方式有误，请检查用例')
            response = None
        return response


if __name__ == '__main__':
    print(YamlToCase('../../source/yamls/stockbulletinlist.yaml').requests())