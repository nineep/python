import time

# 装饰器： 高阶函数 +_ 函数嵌套 + 闭包
def timmer(func): # 定义装饰器函数（高阶函数），传入被装饰函数，以便调用执行
    def wrapper(*args, **kwargs):  #定义嵌套函数：函数封装，其实就是调用传入的被装饰函数，在此前后执行一些其他的动作
        start_time = time.time() #被装饰函数调用前执行动作
        res = func(*args, **kwargs) #调用被装饰函数func, 使用了闭包， 将返回值赋值res，以便后续返回
        stop_time = time.time()  #被装饰函数调用后执行动作
        print('函数运行时间：%s' % (stop_time - start_time)) #被装饰函数调用后执行动作
        return res #返回被装饰函数的返回值，必须
    return wrapper #返回封装函数

@timmer
def cal(l):
    res = 0
    for i in l:
        time.sleep(0.1)
        res += i
    return res

res =  cal(range(20))
print(res)

# 普通装饰器
def wrapper(func):
    def inner():
        print('1')
        func()
        print('2')
    return inner

@wrapper
def func():
    print('被装饰的函数')

func()


# 带参数装饰器
# 使用wraps装饰func，私有__doc__,__name__魔法
from functools import wraps
def func2(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print('我是装饰器')
        ret = func(*args, **kwargs)
        return ret
    return inner

@func2
def func1(*args, **kwargs):
    print('我被装饰')

func1()

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