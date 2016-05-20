
import regex
from datetime import datetime as dt
from Helpers import *


src = '中文名,胡锦涛,国    籍,中国,民    族,汉族,出生地,江苏泰州,出生日期,1942年12月,毕业院校,清华大学出生日期,1946年11月,' \
      '毕业院校,厦门大学,主要成就,中央政治局常委，国务院副总理、党组副书记,参加工作,1970年8月,入党时间,1973年12月'
pattern = regex.compile(r'出生日期.+\d{4}年\d{1,2}月')
match = pattern.search(src)
if match:
    date = regex.compile(r'\d{4}年\d{1,2}月')
    birthday = date.search(match.captures()[0])
    print(birthday.captures())

ss = '政治人物,，,元首,，,人物,，,中国'
p = regex.compile(r'，,')
match = p.sub(repl='', string=ss)


class TT:
    @classmethod
    def name(cls):
        return cls.__name__

print(type(config))
