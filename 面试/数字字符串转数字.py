# 字符串 "123" 转换成 123，不使用内置api，例如 int()

# def atoi(s):
#     num = 0
#     for v in s:
#         for j in range(10):
#             if v == str(j):
#                 num = num*10 + j
#     return num
#
# def atoi(s):
#     num = 0
#     for v in s:
#         num = num * 10 + ord(v) - ord('0')
#     return num


# def atoi(s):
#     num = 0
#     for v in s:
#         t = '%s * 1' % v
#         n = eval(t)
#         num = num * 10 + n
#     return num


from functools import reduce
def atoi(s):

print(type(atoi('123')))