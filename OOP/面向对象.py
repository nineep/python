# -*- coding: utf-8 -*-
'''
面向对象三大特性：封装，继承，多态
'''

#封装
#使用构造方法将内容封装到对象中，然后通过对象直接或者self间接获取被封装的内容
class people:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def attr(self):
        print(self.name)
        print(self.age)


p1 = people('xixi', 21)
p2 = people('haha', 23)
print(p1.name, p2.name)
p1.attr()
p2.attr()


#继承
#多个类共有的方法提取到父类中，子类仅需继承父类而不必一以实现每个方法
#子类subclass，父类superclass，也叫派生类，基类

#多继承
#pythn的类可以继承多个类，java，c#中只能继承一个类
#python的类如果继承了多个类， 那么其寻在方法有两种，深度优先，广度优先
#当类是经典类时，多继承情况下，会按照深度优先方式查找
#当类是新式类（object）时，多继承情况下，会按照广度优先方式查找


#多态
#python不支持java，c#这一类强类型语言中多态的写法，但是原生多态，其python崇尚“鸭子类型”
#“当看到一只鸟走起来像鸭子，游泳起来像鸭子，叫起来像鸭子，那么这只鸟可以被称为鸭子。”
#我们并不关心对象是什么类型，到底是不是鸭子，只关心行为
##鸭子类型在动态语言中经常使用，非常灵活，使得python不像java那样专门去弄一大堆的设计模式

class F1:
    pass

class S1(F1):
    def show(self):
        print(S1.show)

class S2(F1):
    def show(self):
        print(S2.show)

def Func(obj):
    print(obj.show())

s1_obj = S1()
Func(s1_obj)
s2_obj = S2()
Func(s2_obj)