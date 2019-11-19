import configparser
from os import path
import pandas as pd
from sqlalchemy import create_engine as ce
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
def read_sql_conf(config_file_path, section):
    cf = configparser.ConfigParser()
    cf.read(config_file_path)
    opt_list = cf.options(section)
    conf_var_list = {}
    for key in opt_list:
        conf_var_list[key] = cf.get(section,key)
    return conf_var_list['engine'] + '+py' + conf_var_list['engine'] + '://' + conf_var_list['user'] + ':' + conf_var_list['password'] + '@' + conf_var_list['host'] + ':' + conf_var_list['port'] + '/' + conf_var_list['db'],conf_var_list['table']
def read_sql_df(config_file_path, section):
    conf_sql = read_sql_conf(config_file_path, section)
    con = ce(conf_sql[0])
    return pd.read_sql_table(conf_sql[1],con)
def save_sql_df(df,config_file_path, section):
    conf_sql = read_sql_conf(config_file_path, section)
    con = ce(conf_sql[0])
    df.to_sql(conf_sql[1], con=con, if_exists='replace')# flavor=conf_sql[0].split('+')[0])
class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        yield self.match
        raise StopIteration

    def match(self, *args):
        if self.fall or not args:
            return True
        elif self.value in args:
            self.fall = True
            return True
        else:
            return False

