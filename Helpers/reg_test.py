
import regex
from datetime import datetime as dt


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


def para_test(*args):
    args = args[0]
    print(type(args))
    print(args)
    return ['haha']
    yield ('hehe')


class Tr:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(args)
        args = (3, 4, 5)
        self.func(*args)


@Tr
def spam(*args):
    print('spam: ', args)
    c = 0
    for i in args:
        c += i
    print(c)


def para(*args):
    print(args)

t = (2, 3, 4)
para(*t)
