# def cascade(n):
#     if n < 10:
#         print(n)
#     else:
#         print(n)
#         cascade(n // 10)
#         print(n)
# cascade(123)

# def cascade2(n):
#     print(n)
#     if n > 10:
#         cascade2(n // 10)
#         print(n)
# cascade2(123)

# def fib(n):
#     if n ==0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-2) + fib(n-1)
# print(fib(768))


def count_partitions (n, m) :
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n-m, m)
        without_m = count_partitions(n, m-1)
        return with_m + without_m
result = count_partitions (5, 3)