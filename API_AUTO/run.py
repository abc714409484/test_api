# -*- conding:utr-8 -*-
#@Time  :2018/11/16 21:36
#@Author:GYP测试
#@File  :run.py

import unittest
import HTMLTestRunner
from tools.project_path import *

from tools.http_test import TestHttp
suite=unittest.TestSuite()


loader=unittest.TestLoader()

suite.addTest(loader.loadTestsFromTestCase(TestHttp))

with open(html_repot_path,'wb')  as file:
    runner=HTMLTestRunner.HTMLTestRunner(
        stream=file,
        title='这个是接口自动化的测试报告',
        description='我来测试哦！',
        tester='GYP')
    runner.run(suite)


