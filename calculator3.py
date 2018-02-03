# -*- coding: utf-8 -*-
import sys
import csv # 用于写入CSV文件

# 处理命令行参数类

class Args(object):
    def __init__(self):
        self.args = sys.argv[1:]
            configfile = args[args.index('-c')+1]
            userfile = args[args.index('-d')+1]
            gongzi_file = args[args.index('-o')+1]
#配置文件类
class Config(object):
    def __init__(self):
        self.config = self._read_config()
    def _read_config(self):
        config = {}
        """
        读取配置文件并写入到config字典中，使用strip()和split()去掉
        配置文件空格和切分。
        """
        with open(configfile, 'r') as cfg_file:
            for cfg in cfg_file.readlines():
                if '=' in cfg:
                    cfg_list = cfg.split('=')
                    self._config[cfg_list[0].strip()] = float(cfg_list[1].strip())
    def get_config:
        return self._config[config_name]
    def get_insurate:
        return(
            self._config['YangLao'],
            self._config['YiLiao'],
            self._config['ShiYe'],
            self._config['GongShang'],
            self._config['ShengYu'],
            self._config['Gongjijin']
        )
class UserData(object):
    def __init__(self):
        self.userdata = self._read_user_data()
    # 用户数据读取内部函数
    def _read_users_data(self):
        userdata = []
        with open(userfile, 'r') as user_file:
            for user in user_file.readlines():
                if ',' in user:
                    user_id, salary = user.strip().split(',')
                    userdata.append((user_id,salary))
        return userdata
    def __iter__(self):
        return iter(self.userdata)

class IncomeTaxCalculator(object):
    #计算每位员工的税后工资  
               
