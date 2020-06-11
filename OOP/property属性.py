class Foo:
    @property
    def AAA(self):
        print('get')

    @AAA.setter
    def AAA(self, val):
        print('set')

    @AAA.deleter
    def AAA(self):
        print('del')

f1 = Foo()
f1.AAA='aaa'
del f1.AAA
