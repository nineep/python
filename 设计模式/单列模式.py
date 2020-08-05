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