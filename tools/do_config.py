# -*- conding:utr-8 -*-
#@Time  :2018/11/17 11:21
#@Author:GYP测试
#@File  :do_config.py

import configparser
class ReadConfig:
    def read_config(self,file_name,section,option):
        cf=configparser.ConfigParser()
        cf.read(file_name,encoding='utf-8')
        return cf.get(section,option)
if __name__ == '__main__':
    res=ReadConfig().read_config('case.config','MODE','file_name')
    print(res)

