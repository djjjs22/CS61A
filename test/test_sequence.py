# def count(s,value):
#     # 返回value在s列表中出现的次数
#     total,index=0,0
#     while index < len(s):
#         if value == s[index]:
#             total += 1
#         index += 1
#     return total
from distutils.dep_util import newer

# def count(s,value):
#     # 返回value在s列表中出现的次数
#     total=0
#     for element in s:
#         if element == value:
#             total += 1
#     return total

# pairs = [[1,2],[2,2],[2,3],[4,4]]
# same_count = 0
# for x,y in pairs:
#     if x == y:
#         same_count += 1
# print(same_count)


# def cheer():
#     for _ in range(3):
#         print("go")
# cheer()

# def divisors(n):
#     return [1]+[(x+1) for x in range(2,n) if n % x==0]
# print(divisors(4))

# odds = [1,3,5,7,9]
# # print(list(range (1,3)))
# # print([odds[i] for i in range(1,3)])
# print(odds[1:3])#包括上限，不包括下限
# print(odds[1:])#从索引1开始切片
# print(odds[:3])#从开始切片到索引2
# print(odds[:])

# print(max(range(10),key=lambda x:7 - (x - 4) * (x - 2)))
# print((lambda x: 7 - (x - 4) * (x - 2))(3))
# print((lambda x: 7-(x-4)*(x-2)) ( 6 ))

nums = [1, 2, 3, 4, 5]
new_nums = {num : num ** 2 for num in nums if num % 2 == 0}
new_nums1 = {num  ** 2: num for num in nums if num % 2 == 0}
print(new_nums)
print(new_nums1)