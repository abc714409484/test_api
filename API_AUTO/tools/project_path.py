# -*- conding:utr-8 -*-
#@Time  :2018/11/17 13:46
#@Author:GYP测试
#@File  :project_path.py

import os
from tools.do_config import ReadConfig

# class Get_Path:
#     def get_path(self):
path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]


case_config_path=os.path.join(path,'conf','case.config')

data_file_name=ReadConfig().read_config(case_config_path,'MODE','file_name')
test_data_path=os.path.join(path,'test_data',data_file_name)
html_repot_path=os.path.join(path,'test_result','html_report','test_api.html')
print(case_config_path)
print(html_repot_path)