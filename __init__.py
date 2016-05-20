
import configparser


__all__ = ['CONFIG_SECTION_ENTITY', 'CONFIG_SECTION_PG', 'CONFIG_SECTION_POLITICIAN_NAMES', 'CONFIGURATION']
CONFIG_SECTION_ENTITY = 'entity'
CONFIG_SECTION_PG = 'postgresql'
CONFIG_SECTION_POLITICIAN_NAMES = 'politicians'

CONFIGURATION = configparser.ConfigParser()
CONFIGURATION.read(filenames='../config.ini', encoding='utf-8')
