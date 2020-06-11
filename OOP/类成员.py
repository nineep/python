# -*- coding: utf-8 -*-

'''
以下为某博客文章中的定义，对于字段和属性的分类本人存在异议
类成员可分为三大类： 字段，方法，属性
    字段(变量)：普通字段，静态字段     #确切的书应该是属性
    方法：普通方法，类方法，静态方法    #除了classmethod，staticmethod，property也应该归咎于方法，毕竟都是作用于方法的装饰器
    属性：普通属性                    #专指@property，感觉此分类不正确

本人理解：
类成员：属性(变量)，方法
    属性：
        类属性（在类中定义，全局作用域）
        类方法属性（在类方法中定义，亦即实例属性，局部作用域）
        类方法转换的属性（使用@property将方法装饰为属性）
    方法：
        普通方法（带有self参数的函数，self是和类联系的关键）
        类方法（使用@classmethod装饰的普通方法，self参数换为cls，cls使用类属性(变量)）
        静态方法（使用@staticmethod装饰的普通方法，不需要self参数，故切断了与类的传参联系，但是可用类调用静态方法）
        魔法（类似__init__的类内置方法，个人认为是元方法）

类成员转换：
    属性是简单的数据类型对象的赋值，方法是复杂函数对象的赋值，故只能将复杂转为简单
    使用 @property， 将方法 转换为 属性

实例对象（唯一操作属性：引用）
    数据属性（类似其他语言的实例变量，数据成员）
    方法

'''

# 字段
# 静态字段=全局变量
# 普通字段 = 局部变量
class Province:
    # 静态字段
    country = '中国'

    def __init__(self, name):

        #普通字段
        self.name = name

# 直接访问普通字段
obj=Province('haha')
print(obj.name)

# 直接访问静态字段
print(Province.country)


# 方法
# 静态方法
class people(object):

    def __init__(self, name):
        self.name = name

    # 由类调用，无默认参数
    @staticmethod
    def eat():
        print('%s is eating')

d = people('tom')
#静态，方法和class无关，只是能调用，其中作用域被隔断，参数什么无法传递
d.eat()

# 类方法
class people(object):
    name = '我是类变量，类字段'
    def __init__(self, name):
        self.name = name

    #由类调用，至少一个cls参数
    #执行类方法时，自动将调用该方法的类复制给cls
    @classmethod
    def eat(cls):
        print('%s is eating' % cls.name)

p = people('tom')
#传递cls.name=people.name给eat参数，只能使用类的变量
p.eat()


# 属性
# 属性由方法变种而来，如果python中没有属性，防范完全可以代替其功能
# 属性存在的意义： 访问属性时可以制造出和访问字段完全相同的假象

class people:
    def func(self):
        print('普通属性')

    #定义属性
    @property
    def prop(self):
        print('property属性调用')

p = people()
p.func()
p.prop

# 属性的两种定义方式，一般使用装饰器方式@property
#装饰器：即在方法上应用装饰器
#静态字段：即在类中定义值为property对象的静态字段

#装饰器方式 实现 属性
class people:
    #定义属性
    @property
    def prop(self):
        return 'tom'

p = people()
result = p.prop
print(result)

class product(object):
    @property
    def price(self):
        print('@property')

    @price.setter
    def price(self, value):
        print('@property.setter')

    @price.deleter
    def price(self):
        print('@price.deleter')

obj = product()
obj.price #自动执行@property修饰的price方法，并获取返回值
obj.price = 123 #自动执行@property.setter修饰的price方法，并将123赋值给方法的参数
del obj.price #自动执行@price.deleter修饰的price方法


#类的特殊方法，魔法
# __doc__
class Foo:
    '''Foo class 描述信息'''
    def func(self):
        pass
print(Foo.__doc__)

#__init__
class Foo2:
    def __init__(self, name):
        self.name = name
        self.age = 18
obj = Foo2('hehe')
print(obj.name, obj.age)

#__call__
class Foo3:
    def __init__(self):
        pass
    def __call__(self, *args, **kwargs):
        print('__call__')
obj = Foo3() #执行__init__
obj()   #执行__call__

#__dict__
class Province:
    country = 'CN'
    def __init__(self, name, count):
        self.name = name
        self.count = count

    def func(self, *args, **kwargs):
        print('func')

print(Province.__dict__)

obj1 = Province('hebei', 1000)
print(obj1.__dict__)

obj2 = Province('henan', 2000)
print(obj2.__dict__)

#__str__
class Foo4:
    def __str__(self):
        return 'haha'
obj = Foo4()
print(obj)

#__getitem__, __setitem__, __delitem__
class Func(object):
    def __getitem__(self, key):
        print('__getitem__', key)
    def __setitem__(self, key, value):
        print('__setitm__', key, value)
    def __delitem__(self, key):
        print('__delitem__', key)
obj = Func()
result=obj['k1']
obj['k2'] = 'haha'
del obj['k1']

#__getslice__, __setslice__, __delslice__

#__iter__
class Foo5(object):
    def __init__(self, sq):
        self.sq = sq

    def __iter__(self):
        return iter(self.sq)

obj = Foo5([1,2,3,4])
print(obj)
for i in obj:
    print(i)


## 类的创建的两种方式
#普通方式
class Foo(object):
    def func(self):
        print('haha')

#type类的构造函数(即type创建类)
def func(self):
    print('hha')
Foo = type('Foo', (object,), {'func': func})

