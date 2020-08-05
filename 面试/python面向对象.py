# Python中类方法、类实例方法、静态方法有何区别？
"""
类方法: 是类对象的方法，在定义时需要在上方使用 @classmethod 进行装饰,形参为cls，表示类对象，类对象和实例对象都可调用
类实例方法: 是类实例化对象的方法,只有实例对象可以调用，形参为self,指代对象本身;
静态方法: 是一个任意函数，在其上方使用 @staticmethod 进行装饰，可以用对象直接调用，静态方法实际上跟该类没有太大关系
"""

# 对面向对象的理解
'''
面向对象是相对于面向过程而言的，
面向过程语言是一种基于功能分析的，以算法为中心的程序设计方法，
面向对象是一种基于结构分析的，以数据为中心的程序设计思想， 面向对象：类：封装，继承，多态
'''



# 遍历一个object的所有属性，并print每一个属性名
class Car:
    def __init__(self, name, loss):  # loss [价格，油耗，公里数]
        self.name = name
        self.loss = loss

    def getName(self):
        return self.name

    def getPrice(self):
        # 获取汽车价格
        return self.loss[0]

    def getLoss(self):
        # 获取汽车损耗值
        return self.loss[1] * self.loss[2]


Bmw = Car("宝马", [60, 9, 500])  # 实例化一个宝马车对象
print(getattr(Bmw, "name"))  # 使用getattr()传入对象名字,属性值。
print(dir(Bmw))  # 获Bmw所有的属性和方法


# 写一个类，尽可能多支持操作符
class Array:
    __list = []
    def __init__(self):
        print('constructor')

    def __del__(self):
        print('destruct')

    def __str__(self):
        return 'this self-defined array class'

    def __getitem__(self, key):
        return self.__list[key]

    def __len__(self):
        return len(self.__list)

    def Add(self, value):
        self.__list.append(value)

    def Remove(self, index):
        del self.__list[index]

    def DisplayItem(self):
        print('Show all items')
        for item in self.__list:
            print(item)


# 请描述抽象类和接口类的区别和联系
"""
1.抽象类： 规定了一系列的方法，并规定了必须由继承类实现的方法。由于有抽象方法的存在，所以抽象类不能实例化。可以将抽象类理解为毛坯房，门窗，墙面的样式由你自己来定，所以抽象类与作为基类的普通类的区别在于约束性更强

2.接口类：与抽象类很相似，表现在接口中定义的方法，必须由引用类实现，但他与抽象类的根本区别在于用途：与不同个体间沟通的规则，你要进宿舍需要有钥匙，这个钥匙就是你与宿舍的接口，你的舍友也有这个接口，所以他也能进入宿舍，你用手机通话，那么手机就是你与他人交流的接口

3.区别和关联：

1.接口是抽象类的变体，接口中所有的方法都是抽象的，而抽象类中可以有非抽象方法，抽象类是声明方法的存在而不去实现它的类

2.接口可以继承，抽象类不行

3.接口定义方法，没有实现的代码，而抽象类可以实现部分方法

4.接口中基本数据类型为static而抽象类不是
"""


# Python中如何动态获取和设置对象的属性
class Parent:
    pass
if hasattr(Parent, 'x'):
    print(getattr(Parent, 'x'))
else:
    setattr(Parent, 'x', 3)
print(getattr(Parent, 'x'))


# python中的可变对象和不可变对象
"""
不可变对象，该对象所指向的内存中的值不能被改变。当改变某个变量时候，由于其所指的值不能被改变，相当于把原来的值复制一份后再改变，这会开辟一个新的地址，变量再指向这个新的地址。

可变对象，该对象所指向的内存中的值可以被改变。变量（准确的说是引用）改变后，实际上其所指的值直接发生改变，并没有发生复制行为，也没有开辟出新的地址，通俗点说就是原地改变。

Pyhton中，数值类型(int 和float)，字符串str、元祖tuple都是不可变类型。而列表list、字典dict、集合set是可变类型
"""


# python的魔法方法
"""
魔法方法就是给类增加魔力的特殊方法，如果对象实现（重载）了这些方法中的某一个
那么这个方法就会在特殊的情况下被python所调用，你可以定义自己想要的行为，这一切都是自动发生的，
他们经常是双下划线包围命名

__init__构造器，当一个实例被创建时候初始化的方法，但它并不是实例化调用的第一个方法
__new__实例化对象调用的第一个方法，它只取下cls参数，并把其他参数传给__init__
__call__ 让一个类的实例像函数一样被调用
__getitem__定义获取容器中指定元素的行为，相当于self[key]
__getattr__定义当用户试图访问一个不存在属性的时候的行为
__setattr__定义当一个属性被设置的时候的行为
__getattribute__定义当一个属性被访问时候的行为
"""


# 面向对象中实现只读属性
# 讲对象私有化，通过共有方法提供一个读取数据的接口
class person:
    def __init__(self, x):
        self.__age = 10
    def age(self):
        return self.__age

t = person(22)
print(t.age())

# 最好的方法
class MyCls(object):
    __weight = 50

    @property
    def weight(self):
        return self.__weight
mc = MyCls()
print(mc.weight)