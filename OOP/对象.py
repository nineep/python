#-*- encoding: utf-8 -*-
#类：把一类事物的相同的特征和动作整合到一起就是类
#类是一个抽象的概念

#对象：基于类而创建的一个具体事务，
#特征和动作整合到一起

# school = {
#     'name': 'haha',
#     'addr': 'beijing',
#     'type': 'sili'
# }
#
# def kao_shi(school):
#     print('%s 学校在考试' %school['name'])
#
# def zhao_sheng(school):
#     print('%s %s 正在招生' % (school['type'], school['name']))


# class Chinese:
#     dang = 'haha'
#
#     def sui_di_tu_tan(self):
#         print('吐痰')
#
#     def cha_dui(self):
#         print('插队')
#
#
# print(Chinese.dang)
# print(Chinese.__dict__)
#
# a = Chinese()
# a.sui_di_tu_tan()

# country = 'China'
# class Chinese:
#     country = '日本'
#     def __init__(self, name):
#         # country = '日本'
#         # print('类实例化')
#         self.name = name
#         print(self.country)
#
#     def play_ball(self, ball):
#         print('%s 正在打 %s' %(self.name, ball))
# p1 = Chinese('nineep')

# name = 'nineep'
# def people():
#     print(%s is teacher %name)


class Vehicle:
    Country = 'China'
    def __init__(self, name, speed, load, power):
        self.name = name
        self.speed = speed
        self.load = load
        self.power = power

    def run(self):
        print('开动啦')

class Subway(Vehicle):
    def __init__(self, name, speed, load, power, line):
        #Vehicle.__init__(self, name, speed, load, power)
        super().__init__(name, speed, load, power)
        self.line = line

    def show_info(self):
        print(self.name, self.speed, self.load, self.power, self.line)

    def run(self):
        #Vehicle.run(self)
        super().run()
        print('%s %s线，开动啦' %(self.name, self.line))

line13 = Subway('北京地铁', '10km/h', 10000, '20', 13)

line13.run()
line13.show_info()
