# -*- conding:utr-8 -*-
#@Time  :2018/11/16 21:50
#@Author:GYP测试
#@File  :http_requests.py

import requests
class Http_Request:
    def request(self,method,url,data,cookie=None):
        try:
            if method == 'post':
                res=requests.post(url,data,cookies=cookie)
            else:
                res=requests.get(url,data,cookies=cookie)
        except Exception as e:
            print("非法请求，请检查{0}".format(e))
            raise e
        return res

