# 设计模式理解
"""
设计模式是经过总结，优化的，对我们经常会碰到的一些编程问题的可重用的解决方案
一个设计模式并不像一个类或一个库那样 能够直接作用于代码，
反之，设计模式更为高级，它是一种必须在特定情形下实现的一种方法模板。
常见的是工厂模式和单例模式
"""

# 单例模式
# 单例模式应用场景
""""
资源共享的情况下，避免由于资源操作时导致的性能或损耗等，如日志文件，应用配置
控制资源的情况下，方便资源之间的互相通信，如线程池等
    网站的计数器，应用配置，多线程池，数据库配置，数据库连接池，日志应用
"""
#使用装饰器
def singleton(cls):
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class Foo(object):
    pass

foo1=Foo()
foo2=Foo()
print(foo1 is foo2)


# 基类New是真正创建实例对象的方法， 重写基类new的方法，
# 以此保证创建对象的时候只生成一个实例
#python3
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

class Foo(Singleton):
    pass
foo1=Foo()
foo2=Foo()
print(foo1 is foo2)

#python2
class A(object):
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance


# 元类是用于创建类对象的类， 类对象创建实例对象时一定要调用call方法，
# 因此在调用call时候保证始终只创建一个实例即可，type是python的元类
class Singleton(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance

#python2
class Foo(object):
    __metaclass__ = Singleton

#python3
class Foo(metaclass=Singleton):
    pass

foo1 = Foo()
foo2 = Foo()
print(foo1 is foo2)




print([x*x for x in range(1,11)])


# 装饰器（高阶函数，参数是函数的函数）
"""
装饰器本质上是一个callable object， 它可以让其他函数在不需要做任何代码变动的前提下增加额外功能
装饰器的返回值也是一个函数对象

装饰器作用：
经常用于有切面需求的场景：插入日志，性能测试，事务处理，缓存，权限校验

有了装饰器就可以抽离出大量的与函数功能本身无关的 雷同的代码并发 并继续使用
"""
import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.clock()
        time.sleep(2)
        ret = func(*args, **kwargs)
        end = time.clock()
        print(end-start)
        return ret
    return wrapper

@timeit
def foo():
    print('in foo()')
foo()


# 闭包
"""
嵌套函数，子函数使用了父函数的变量， 那么子函数和使用到的变量 称为闭包
"""


# 生成器和迭代器区别
"""
迭代器是遵循迭代协议的对象，用户可以使用iter()以从任何序列得到迭代器（如list， tuple， dictionary，set等）
另一个方法则是创建一个另一种形式的迭代器： generator
要获取下一个元素，则使用成员函数next()（python2）或函数next() function (python3),当没有元素时，则引发StopIteration
若要自己实现迭代器，只要实现next()(python2)或__next__()（python3）

生成器（Generator）,只是在需要返回数据的时候使用yield语句，每次next()被调用时，
生成器会返回它脱离的位置（它记忆语句最后一次执行的位置和所有的数据值）

区别：
    生成器能做到迭代器能做的所有事，而且因为自动创建iter()和next()方法，生成器显得特别简洁，而且生成器也是高效的
    使用生成器表达式 取代列表解析 可以同时节省内存
    除了创建和保存程序状态的自动方法，当发生器终结时，还会自动抛出StopIteration
"""
# 生成器示例
x = (i for i in range(10))
x.__next__()
print(type(x))
# 列表表达式
l = [i for i in range(10)]
print(type(l))

# 请用一行代码 实现将1-N 的整数列表以3为单位分组
N = 100
print([[x for x in range(1,100)][i:i+3] for i in range(0, 100, 3)])


# 生成器 yield的用法
"""
yield就是保存当前程序执行状态， 使用for循环的时候，每次取一个元素的时候，九辉计算一次。
使用yield的函数叫generator， 和iterator一样，好处是不用一次计算所有元素，而是用一次算一次，可以节省很多空间
generator每次计算需要上一次计算的结果，所以用yield，不能使用return，否一return，上次结算结果就没了
"""
