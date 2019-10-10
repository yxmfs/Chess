import configparser
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
        conf_var_list[key] = cf.get(section,key)
    return conf_var_list
if __name__ == '__main__':
    print(read_conf_dict('./data/conf.ini','num'))
