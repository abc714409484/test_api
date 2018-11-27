# -*- conding:utr-8 -*-
#@Time  :2018/11/18 15:00
#@Author:GYP测试
#@File  :http_test.py


import unittest  #单元测试框架

from tools.do_excel import Do_Excle   #数据读写
from tools.project_path import *   #文件路径
from ddt import ddt,data  #数据处理框架
from tools.get_data import Get_Data  #反射
from tools.http_requests import Http_Request

test_data=Do_Excle().Read_Excle()  #读取数据
@ddt
class TestHttp(unittest.TestCase):
    @data(*test_data)
    def test_api(self,item):
        res=Http_Request().request(item['method'],item['url'],eval(item['data']),getattr(Get_Data,'cookie'))
        if res.cookies:  #利用反射获取cookie的值
            setattr(Get_Data,'cookie',res.cookies)
        try:
            self.assertEqual(str(item['ExpectedResult']),res.json()['code'])
            ActaulResult='Pass'
        except AssertionError as e:
            print('执行用例失败，请检查%s' %e)
            ActaulResult = 'Faile'
            print("获取到的结果是：{0}".format(res.json()))
        finally:
            # print(item['case_id'])
            Do_Excle.write_excel(test_data_path,item['module'],item['case_id']+1,ActaulResult)











