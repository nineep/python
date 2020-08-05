# 方法一：构造字典
def count_str(str_data):
    dict_str = {}
    for i in str_data:
        dict_str[i] = dict_str.get(i, 0) +1
    return dict_str

dict_str = count_str('AAABBCCAC')
print(dict_str)

str_count_data = ''
for k, v in dict_str.items():
    str_count_data += k + str(v)
print(str_count_data)


# 方法二：
from collections import Counter
ret = ''.join(map(lambda x:x[0] + str(x[1]), Counter('AAABBCCAC').most_common()))
print(ret)