import configparser


def get_config(config_file='config.ini'):
    # 读取config.ini 文本里面的参数设置,返回一个大的字典文件

    parser = configparser.ConfigParser()
    parser.read(config_file)
    # get the ints, floats and strings
    _conf_ints = [(key, int(value)) for key, value in parser.items('ints')]
    _conf_floats = [(key, float(value)) for key, value in parser.items('floats')]
    _conf_strings = [(key, str(value)) for key, value in parser.items('strings')]
    return dict(_conf_ints + _conf_floats + _conf_strings)