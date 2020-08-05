# 推导式可以从一个数据序列构建另一个新的数据序列的结构体

# 列表推导式
"""
使用[]生成list
variable = [out_exp_res for out_exp in input_list if out_exp == 2]

out_exp_res: 列表生成元素表达式，可以是有返回值的函数
for语句： 迭代
if语句：条件过滤
"""

multiples = [i for i in range(30) if i % 3 is 0]
print(multiples, type(multiples))

def squared(x):
    return x*x
multiples = [squared(i) for i in range(30) if i % 3 is 0]
print(multiples, type(multiples))

# 使用（）生成generator
multiples = (i for i in range(30) if i %3 is 0)
print(multiples, type(multiples))



# 字典推导式
# 和列表推导式类似， 区别：使用{}，返回字典
mcase = {'a': 10, 'b': 34, 'A': 7, 'z': 3}
mcase_frequency = {
    k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
    for k in mcase.keys()
    if k.lower() in ['a', 'b']
}
print(mcase_frequency, type(mcase_frequency))

d = {'a': 10, 'b': 34}
# 转换字典key，value顺序
dd = {v:k for k, v in d.items()}
print(dd, type(dd))

# 集合推导式
# 和列表推导式类似， 区别：使用{}， 返回集合。 返回值也会有集合的去重特性
squared = {x**2 for x in [1,1,2]}
print(squared, type(squared))
