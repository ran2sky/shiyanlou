# -*- coding: utf-8 -*-
import sys
import csv 
# 用于写入CSV文件
# 处理命令行参数类
#配置文件类
class Config:
    def __init__(self):
        self._config = {}
        """
        读取配置文件并写入到config字典中，使用strip()和split()去掉
        配置文件空格和切分。
        """
        with open(configfile, 'r') as cfg_file:
            for cfg in cfg_file.readlines():
                if '=' in cfg:
                    cfg_list = cfg.split('=')
                    self._config[cfg_list[0].strip()] = float(cfg_list[1].strip())
    def get_config(self):
        return self._config[config_name]
    def get_insurate(self):
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
        self.userdata = {}
        with open(userDatafile, 'r') as user_file:
            for user in user_file.readlines():
                if ',' in user:
                    usersalary_list = user.split(',')
                    self._userdata[usersalary_list[0]] = float(usersalary_list[1]) 
    # 用户数据读取内部函数
    def get_userdatabyid(self):
        return self._userdata[userID]       
    def get_userdata(self):
        return self._userdata

    #计算每位员工的税后工资  
def calc_for_all_userdata(self):
    JiShuL = config.get_config('JiShuL')
    JishuH = config.get_config('JiShuH')
    user_list = userdata.get_userdata()
    result_dict = {}
    insu_rate = sum(config.get_insurate())
    for user_id, salary in user_list:
        if user_dict[id] > JiShuH:
            insu_part = JiShuH * insu_rate
        elif user_dict[id] < JiShuL:
            insu_part = JiShuL * insu_rate
        else:
            insu_part = user_dict[d] - insu_part - 3500
        if taxed_part <=0:
            tax_result = 0
        if taxed_part <= 1500:
            tax_result = taxed_part*0.03
        elif taxed_part <= 4500:
            tax_result = taxed_part*0.1 - 105
        elif taxed_part <= 9000:
            tax_result = taxed_part*0.2 - 555
        elif taxed_part <= 35000:
            tax_result = taxed_part*0.25 - 1005
        elif taxed_part <= 55000:
            tax_result = taxed_part*0.3 - 2755
        elif taxed_part <= 80000:
            tax_result = taxed_part*0.35 - 5505
        elif taxed_part > 80000:
            tax_result = taxed_part*0.45 - 13505
        income = user_dict[id] - insu_part - tax_result
        result_dict[id] = [format(user_dict[id], '.2f'), format(insu_part, '.2f'), format(tax_result, '.2f'), format(income, '.2f')]
    if saveCSV:
        outputResult(result_dict, gongzifile)
    return result_dict

def outputResult(self):
    with open(gongzifile, 'w') as output:
        for id in result_dict:
            personData = ','.join([str(i) for i in result_dict[id]])
            output.write(str(id) + ',' + personData + '\n')
if __name__ == '__main__':
    args = sys.argv[1:]
    try:
        configfile = args[args.index('-c')+1]
        userfile = args[args.index('-d')+1]
        gongzi_file = args[args.index('-o')+1]
        config = Config(cfg_file)
        userdata = UserData(userData_file)
        calculator(config, userdata, gongzi_file)
    except(IOError):
        print('No such file, please check the file path!')
    except(ValueError):
        print('Patameter Error, Please check he data type!')
    except(NameError):
        print('Please input entire parameter list! e.g. -c xxx -d xxx -o xxx')
