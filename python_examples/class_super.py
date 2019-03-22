
# 类 继承
import random as r

class Fish():
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def mova(self):
        self.x -= 1
        print('position is:', self.x, self.y)

class Shark(Fish):
    def __init__(self):
        # Fish.__init__(self)
        # 父类的方法是可以在子类随便拿来用的，那么对于平辈的类，
        # 也可以相互调用彼此的方法， 这样叫做类的 组合。
        super().__init__()
        self.hangry = True
    
    def eat(self):
        if self.hangry:
            print("eat")
            self.hangry = False
        else:
            print("eat too much")

# 类 组合
class Turtle():
    def __init__(self, x):
        self.num = x

class Fish():
    def __init__(self, x):
        self.num = x

class Pool():
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)
    def print_num(self):
        print("水池有乌龟%d只，鱼%d条!" % (self.tutle.num, self.fish.num))

pool = Pool(3,10)
pool.print_num()


