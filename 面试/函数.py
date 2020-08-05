# 判断时间的装饰器
import datetime
from functools import wraps

def timechecks(func):
    @wraps(func)
    def wrappers(*args, **kwargs):
        if datetime.datetime.now().year == 2020:
            func(*args, **kwargs)
        else:
            print('年代久远')
    return wrappers

@timechecks
def test(name, year):
    print('Hello {}, {}, Happy'.format(name, year))

test('xiaoming', 2020)


# 函数调用参数的传递方式是值传递还是引用传递
"""
python的参数传递有： 位置参数，默认参数，可变参数，关键字参数
不可变参数 用值传递：像整数和字符串这样的不可变对象，是通过拷贝进行传递的，因为你无论如何都不可能在远处改变不可变对象
可变参数 是引用传递: 比如列表，字典这样的对象时通过引用传递
"""


# 带参数的装饰器
# 带定长参数的装饰器
def new_func(func):
    def wrappedfun(username, passwd):
        if username == 'root' and passwd == '123456':
            print('通过认证')
            print('开始执行附加功能')
            return func()
        else:
            print('错误')
            return
    return wrappedfun
@new_func
def origin():
    print('开始执行函数')
origin('root', '123456')

# 带不定长参数的装饰器
def new_func(func):
    def wrappedfun(*args, **kwargs):
        print('我是不定长参数：', args, kwargs)
        if args and kwargs:
            print(len(args), len(kwargs))
        func()
    return wrappedfun

@new_func
def test():
    print('开始测试')

test('haha', 'hehe', {1:'xixi'}, k1='heihei', k2='wuwu')


# map reduce函数
from functools import reduce
print(list(map(lambda x:x*x, [1,2,3,4])))
reduce(lambda x,y: x*y, [1,2,3,4])
print(list(map(lambda x: x*x, [y for y in range(3)])))


# 回调函数，如何通信
"""
回调函数是把函数的指针（地址）作为参数传递给另一个函数， 将整个函数当做一个对象
赋值给调用的函数
"""

# py内建类型：
"""布尔，数字，字符串，列表，元组，集合，字典"""


# hasattr() getattr() setattr()
# hasattr(object, name)函数，判断对象中是否有name属性或者name方法，返回bool值
class function_demo(object):
    name = 'demo'
    def run(self):
        return 'hello function'
function_demo = function_demo()
res = hasattr(function_demo, 'name')
res1 = hasattr(function_demo, 'run')
res2 = hasattr(function_demo, 'age')
print(res,res1,res2)

# getattr(object, name[,default])函数，获取对象object属性或方法，如果存在则打印，不存在则打印默认值，默认值可选
# 如果返回的是对象方法，则打印结果：方法的内存地址
# 如果需要运行这个方法，可以在后面添加括号（）
print(getattr(function_demo, 'name'))
print(getattr(function_demo, 'run'))
print(getattr(function_demo, 'age', 18))

# setattr(object, name, values)函数，给对象的属性赋值，若属性不存在， 先创建再赋值
res = hasattr(function_demo, 'age')
print(res)
setattr(function_demo, 'age', 18)
res1 = hasattr(function_demo, 'age')
print(res1)

# 综合使用
res = hasattr(function_demo, 'addr')
if res:
    addr = getattr(function_demo, 'addr')
    print(addr)
else:
    addr = getattr(function_demo, 'addr', setattr(function_demo, 'addr', '北京'))
    print(addr)


# 阶乘函数 (1*2*3...*9)
print(reduce(lambda x, y: x*y, range(1, 10)))

# lambda
"""
lambda函数是一个可接受任意多个参数（包括可选参数），并且返回单个表达式值的函数
1.lambda函数比较轻便，即用即扔，很适合需要完成一项功能， 但是此功能只在此一处使用， 连名字都很随意的情况下
2.匿名函数，一般用来给 filter，map， reduce这样的函数式编程服务
3.作为回调函数，传递给某些应用，比如消息处理
"""

# 递归函数停止条件
"""
递归的终止条件一般定义在递归函数内部， 在递归函数调用前做一个条件判断，根据判断的结果选择是继续调用自身，还是return，返回终止递归
终止条件： 
判断递归的次数是否达到某一限定值
判断运算的结果是否达到某个范围等， 根据设计目的来选择
"""


# 下面这段代码的输出结果将是什么？请解释
def multipliers():
    return [lambda x: i *x for i in range(4)]
print([m(2) for m in multipliers()])
"""
你如何修改上面的multipliers的定义产生想要的结果？
上述问题产生的原因是python闭包的延迟绑定。这意味着内部函数被调用时，参数的值在闭包内进行查找。
因此，当任何由multipliers()返回的函数被调用时,i的值将在附近的范围进行查找。
那时，不管返回的函数是否被调用，for循环已经完成，i被赋予了最终的值3.
"""
# 正确写法
def multipliers():
    for i in range(4):
        yield lambda x: i*x
print([m(2) for m in multipliers()])

def multipliers():
    return [lambda x,i=i: i*x for i in range(4)]
print([m(2) for m in multipliers()])

