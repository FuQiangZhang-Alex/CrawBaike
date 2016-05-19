
import regex


def sum_num(lst):
    tot = []
    rtn = ''
    items = list(lst)
    while items:
        front = items.pop()
        if not isinstance(front, list):
            tot.append(front)
        else:
            items.extend(front)
    # print(tot)
    while tot:
        item = str(tot.pop())
        rtn += item
    return rtn


def large_sum(lst):
    tot = 0
    items = list(lst)
    while items:
        top = items.pop()
        tot += top
    return tot


def u_match(src):
    pattern = regex.compile(u'')
    t = pattern.search(src)
    print(t)

lt = ['1', '2', '3', ['s', 'b', ['hah', 'hehe'], 'c', 'd'], '4', '5']
t = sum_num(lt)
# print(t)
u_match('习 平')
# it is better to use loop instead of recursing when processing large amount of data
# large = [i for i in range(1, 1000000)]
# print(large_sum(large))

