
# l = []
# nums = [2, 7, 11, 15, 1, 8, 7]
# for a in nums:
#     for b in nums:
#         if a + b == 9:
#             t = (a, b)
#             l.append(t)
# print(l)


# map()
# filter()
# from functools import reduce
# reduce()
# sorted()
# print()


# ls = [1, 2, 3, 4]
# iter_ls = ls.__iter__()
# while True:
#     try:
#         print(iter_ls.__next__())
#     except StopIteration:
#         print('迭代完毕，循环终止')
#         break

# def xia_dan():
#     ret = []
#     for i in range(100):
#         ret.append('ji_dan%s' % i)
#     return ret
#
#
# print(xia_dan())


# def xia_dan():
#     for i in range(10000):
#         yield 'ji_dan%s' % i
#
# muji = xia_dan()
# jidan = muji.__next__()
# jidan = muji.__next__()
# jidan = muji.__next__()
# jidan = muji.__next__()
# jidan = muji.__next__()
#
# print('mai ji dan', jidan)


# def test():
#     print('开始')
#     first = yield
#     print('第一次', first)
#     yield 2
#     print('第二次')
#
# t = test()
# res=t.__next__()
# print(res)
# t.send('send_value')


# s = input('输入：')
#
# def alpha_num_count(s):
#     res_dict = {}
#
#     int_count = 0
#     upper_count = 0
#     lower_count = 0
#
#     for i in s:
#         if i.isupper():
#             int_count += 1
#         elif i.islower():
#             lower_count += 1
#         else:
#             upper_count += 1
#
#     res_dict['int_num'] = int_count
#     res_dict['lower_num'] = lower_count
#     res_dict['upper_num'] = upper_count
#
#     return res_dict
#
# print(alpha_num_count(s))

# def func(x, y, z=5):
#     print(x, y, z)
# func(1, 2, 3)

