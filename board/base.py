import configparser
from os import path
import numpy as np
import pandas as pd
def read_conf_dict(config_file_path, section):
    '''
    description:
        Return the var of variable, according to the config file.
    input:
        config_file_path: str, the path of config file
        section: str, the section where variable is
    output:
        dict, all of var
    '''
    cf = configparser.ConfigParser()
    cf.read(config_file_path)
    opt_list = cf.options(section)
    conf_var_list = {}
    for key in opt_list:
        conf_var_list[key] = int(cf.get(section,key))
    return conf_var_list
def conf_reader(config_file_path,section):
    if path.isfile(config_file_path):
        return read_conf_dict(config_file_path,section)
    else:
        print('Can not read the conf file,load the default values!')
        return {
                'min_x' : 0,
                'max_x' : 8,
                'min_y' : 0,
                'max_y' : 9,
                'red_min_x' : 0,
                'red_max_x' : 4,
                'blk_min_x' : 5,
                'blk_max_x' : 9,
                }
class BaseBoard():
    def __init__(self,):
        self.__conf_dict = conf_reader('./data/conf.ini','num')
        t_s = 'no'
        temp_list = [(t_s,t_s,t_s) for _ in range(self.__conf_dict['max_y']+1)]
        temp_dict = {}
        for key in range(self.__conf_dict['max_x']+1):
            temp_dict[str(key)] = temp_list
        self.__status = pd.DataFrame(temp_dict)
        self.__sort_dict = {0:'boss',1:'car',2:'horse'}
    def get_status(self,):
        print(self.__status.shape)
        return self.__status
    def init_status(self,):
        self.__status['0'][0] = ('car','r',0)
        self.__status['8'][0] = ('car','r',1)
        self.__status['1'][0] = ('horse','r',0)
        self.__status['7'][0] = ('horse','r',1)
        self.__status['2'][0] = ('minister','r',0)
        self.__status['6'][0] = ('minister','r',1)
        self.__status['3'][0] = ('guard','r',0)
        self.__status['5'][0] = ('guard','r',1)
        self.__status['4'][0] = ('boss','r',0)
        self.__status['1'][2] = ('cannon','r',0)
        self.__status['7'][2] = ('cannon','r',1)
        self.__status['0'][3] = ('soldier','r',0)
        self.__status['2'][3] = ('soldier','r',1)
        self.__status['4'][3] = ('soldier','r',2)
        self.__status['6'][3] = ('soldier','r',3)
        self.__status['8'][3] = ('soldier','r',4)

        self.__status['0'][9] = ('car','b',0)
        self.__status['8'][9] = ('car','b',1)
        self.__status['1'][9] = ('horse','b',0)
        self.__status['7'][9] = ('horse','b',1)
        self.__status['2'][9] = ('minister','b',0)
        self.__status['6'][9] = ('minister','b',1)
        self.__status['3'][9] = ('guard','b',0)
        self.__status['5'][9] = ('guard','b',1)
        self.__status['4'][9] = ('boss','b',0)
        self.__status['1'][7] = ('cannon','b',0)
        self.__status['7'][7] = ('cannon','b',1)
        self.__status['0'][6] = ('soldier','b',0)
        self.__status['2'][6] = ('soldier','b',1)
        self.__status['4'][6] = ('soldier','b',2)
        self.__status['6'][6] = ('soldier','b',3)
        self.__status['8'][6] = ('soldier','b',4)

if __name__ == '__main__':
    print(conf_reader('./data/conf.ini','num'))
    bb = BaseBoard()
    bb.init_status()
    print(bb.get_status())
