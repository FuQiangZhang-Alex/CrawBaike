
from Spiders.BaikeSpider import PoliticianExtractor
from Items.Person import Person
import regex
from Helpers.PGHelper import PG
from datetime import datetime as dt
from Helpers import *


persons = []


def list2str(lst):
    """
    convert list items to string
    :param lst: list to be converted
    :return: list's items' string separated by ','
    """
    _lst_str = ''
    for item in lst:
        _lst_str += str(item) + ','
    return _lst_str.rstrip(',')


def extractor():
    """
    extract politician basic information from crawled html page
    save politician directly into database
    :return: nothing
    """
    bs = PoliticianExtractor(config_file='../config.ini')
    politician_dict = bs.info_dict()
    pg = PG()
    for key in politician_dict.keys():
        print('###########################', key, '###########################')
        politician = politician_dict[key]  # a single politician
        name = str(key).split(';')[0]  # get politician name
        source_url = str(key).split(';')[1]  # get source URL
        person = extract_info_from_politician(politician, name, source_url)
        # persons.append(person)
        status = person.save(db_helper=pg.save, tbl_name=config['entity'][person.name()])  # save person into database
        print(status)
        print()


def extract_info_from_politician(content_list=None, name=None, source_url=None):
    if content_list is None or name is None or source_url is None:
        return None
    politician = list(content_list.copy())
    reg_dict = {
        'date_duration': regex.compile(r'[12]\d{3}[—－][12]\d{3}'),
        'birthday': regex.compile(r'(?<=出生日期.)\d{4}年\d{1,2}月'),
        'alias': regex.compile(r'(?<=别    名,).+?(?=,)'),
        'english_name': regex.compile(r'(?<=英文名,).+?(?=,)'),
        'gender': regex.compile(r'(?<=' + name + r'[，  ])' + r'[男女]'),
        'hometown': regex.compile(r'((?<=籍    贯,).+?(?=,))|((?<=出生地,).+?(?=,))'),
        'tag': regex.compile(r'(?<=词条标签：,).+$')
    }
    person = Person()  # politician entity
    person['NAME'] = name  # politician name
    person['SOURCEURL'] = source_url  # source url
    # process each line to extract other information
    for line in politician:
        line_str = str(list2str(line))

        # extract birthday
        birthday = reg_dict['birthday'].search(line_str)
        if birthday:
            y = int(regex.search('\d{4}(?=年)', str(birthday.captures()[0])).captures()[0])
            m = int(regex.search('\d{1,2}(?=月)', str(birthday.captures()[0])).captures()[0])
            person['BIRTHDAY'] = dt(year=y, month=m, day=1).date()

        # extract alias
        alias = reg_dict['alias'].search(line_str)
        if alias:
            person['ALIAS'] = alias.captures()[0]

        # extract english name
        english_name = reg_dict['english_name'].search(line_str)
        if english_name:
            person['ENGLISHNAME'] = english_name.captures()[0]

        # extract gender
        gender = reg_dict['gender'].search(line_str)
        if gender:
            person['GENDER'] = gender.captures()[0]

        # extract age
        # calculated by birthday
        if 'BIRTHDAY' in person:
            pp = regex.search(r'^\d{4}', str(person['BIRTHDAY']))
            if pp:
                birthday_year = int(pp.captures()[0])
                now_year = int(dt.now().year)
                person['AGE'] = now_year - birthday_year

        # extract hometown
        hometown = reg_dict['hometown'].search(line_str)
        if hometown:
            person['HOMETOWN'] = hometown.captures()[0]

        # extract tag
        tag = reg_dict['tag'].search(line_str)
        if tag:
            person['TAG'] = str(regex.sub(pattern=r'，,', repl='', string=str(tag.captures()[0])))

        # create date
        person['CREATEDATE'] = dt.now().date()

        # extract political experience
        # first, extract date duration
        date_duration = reg_dict['date_duration'].search(line_str)
        if date_duration:
            duration_line = date_duration.captures()
            # print(line_str)
    return person

extractor()
