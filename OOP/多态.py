# -*- coding: utf-8 -*-


class H2O:
    def __init__(self, name, temperature):
        self.name = name
        self.temperature=temperature

    def turn_ice(self):
        if self.temperature < 0:
            print('[%s]温度太低结冰了' % self.name)
        elif self.temperature > 0 and self.temperature < 100:
            print('[%s]液化成水' % self.name)
        elif self.temperature > 100:
            print('[%s]温度太高变成了水蒸气' % self.name)


class Water(H2O):
    pass


class Ice(H2O):
    pass


class Steam(H2O):
    pass

len()