

import configparser

__all__ = ['config']

config = configparser.ConfigParser()
config.read(filenames='../config.ini', encoding='utf-8')
