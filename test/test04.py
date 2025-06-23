# def count_partitions(n,m):
#     if n < m or m == 0:
#         return 0
#     else:
#         exact_match = 0
#         if n == m:
#             exact_match = 1
#         with_m = count_partitions(n - m, m)
#         without_m = count_partitions(n, m - 1)
#         return exact_match + with_m + without_m
# print(count_partitions(6,4))

# def list_count_partitions(n,m):
#     if n < m or m == 0:
#         return []
#     else:
#         exact_match = []
#         if n == m:
#             exact_match = [[m]]
#         with_m = [p + [m] for p in list_count_partitions(n - m, m)]
#         without_m = list_count_partitions(n, m - 1)
#         return exact_match + with_m + without_m
# print(list_count_partitions(6,4))

def partitions(n,m):
    if n > 0 and m > 0:
        if n == m:
            yield str(m)
        for p in partitions(n - m, m):
            yield p + '+' + str(m)
        yield from partitions(n, m - 1)
t = list(partitions(6,4))
print(next(t))