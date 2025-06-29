def Link(g,s):

def square(x):
    return x * x

def odd(x):
    return x % 2 == 1

def empty_link():
    # return

def range_link(start,end):
    # 返回一个从开始到结束包含连续整数的链表
    # range_link（3,6）-> Link(3,Link(4,Link(5)))
    if start >= end:
        return empty_link
    else:
        return range_link(start,range_link(start + 1,end))

def map_link(f,s):
    if s is empty_link():
        return s
    else:
        return Link(f(s.first),map_link(f,s.rest))
def filter_link(f,s):
    if s is empty_link():
        return s
    filter_rest = filter_Link(f,s.rest)
    if f(s.first):
        return Link(s.first,filter_rest)
    else:
        return filter_rest