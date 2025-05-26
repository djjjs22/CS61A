from operator import mul, add
from turtledemo.penrose import f

import end


#
# def delay(arg):
#     print('delayed')
#     def g():
#         return arg
#     return g
#
# delay(delay)()(6)()
# print(delay (print) () (4))


def square(x):
    return mul(x, x)
#
# def pirate(arggg):
#     print ('matey')
#     def plunder(arggg):
#         return arggg
#     return plunder
#
# b = add(pirate(3)(square)(4),1)
# print (b)
# def pirate(argggg):
#     print('matey')
#     def plunder(ignored_arg):  # 参数被忽略，直接返回闭包中的 argggg
#         return argggg
#     return plunder
#
# def add(a):
#     def inner(b, c):
#         return a + b + c
#     return inner
#
# result = add(pirate(3)(square))(square(4), 1)
# print(result)  # 输出 20（假设 add 实现为柯里化的三元加法）


# def curried_pow(x):
#         def h(y):
#             return pow(x, y)
#         return h
# a = curried_pow(2)(3)
# print(a)

