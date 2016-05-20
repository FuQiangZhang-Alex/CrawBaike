
from Spiders.CrawlSpider import CrawlSpider
import urllib3
from .. import *


class PoliticianExtractor:
    # store all politicians given by the configuration file
    politicians = {}

    def __init__(self):
        pass

    @staticmethod
    def process_line(line):
        if '\n' in line and len(line) > 1:
            str_list = line.split('\n')
            return str_list
        elif len(line) > 1:
            return line
        else:
            return None

    @staticmethod
    def remove_none_in_list(lst):
        while None in lst:
            lst.remove(None)
        return lst.copy()

    @staticmethod
    def remove_empty_str_in_list(lst):
        while '' in lst:
            lst.remove('')
        return lst.copy()

    @staticmethod
    def list2str(lst):
        _lst = []
        _lst_str = ''
        items = PoliticianExtractor.remove_empty_str_in_list(PoliticianExtractor.remove_none_in_list(list(lst)))
        while items:
            top = items.pop()
            if not isinstance(top, list):
                _lst.append(top)
            else:
                top = PoliticianExtractor.remove_empty_str_in_list(PoliticianExtractor.remove_none_in_list(top))
                items.extend(top)
        while _lst:
            top = _lst.pop()
            # /\u\s/
            _lst_str = _lst_str + str(top) + ' '
        return _lst_str

    @staticmethod
    def unpack(lst):
        _lst = []
        items = PoliticianExtractor.remove_empty_str_in_list(PoliticianExtractor.remove_none_in_list(list(lst)))
        while items:
            top = items.pop()
            if not isinstance(top, list):
                _lst.append(top)
            else:
                top = PoliticianExtractor.remove_empty_str_in_list(PoliticianExtractor.remove_none_in_list(top))
                items.extend(top)
        _lst.reverse()
        return _lst

    @staticmethod
    def process_html(html):
        x = '/html/body/descendant::div[@class="main-content"]/child::div'
        content = html.xpath(x)
        politician = []
        for element in content:
            lines = element.itertext()
            text = list(map(PoliticianExtractor.process_line, lines))
            text_list = PoliticianExtractor.unpack(text)
            if text_list:
                politician.append(text_list)
        return politician

    def info_dict(self):
        names = CONFIGURATION[CONFIG_SECTION_POLITICIAN_NAMES]['names']
        names = str(names).split(',')
        h = 'baike.baidu.com'
        sp = CrawlSpider(host=h)
        for name in names:
            name.encode(encoding='utf-8')
            parameter = {'word': name}
            url_para = urllib3.request.urlencode(parameter)
            p = '/search/word?' + url_para
            source_url = h + p
            sp.path = p
            poli = sp.extract(self.process_html)
            key = name + ';' + source_url
            self.politicians[str(key)] = poli
        return self.politicians.copy()
