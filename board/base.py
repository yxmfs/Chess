import configparser
from os import path
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
if __name__ == '__main__':
    print(conf_reader('./data/conf.ini','num'))
