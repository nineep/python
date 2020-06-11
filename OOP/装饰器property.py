'''
关于property
    类的方法调用需要__call__方法，调用时加（）
    类的属性直接访问Class.属性即可，不需要（）
@property装饰器创建的方法，会将方法转换成同名的制度属性，
可以与所定义的属性配合使用，防止属性被修改
'''

## 使用场景

#修饰方法，使方法可以像属性一样访问
class DataSet(object):

    # property修饰的方法只有self默认参数，故方法固定无法改变
    @property
    def method_with_property(self):
        return 15

    def method_without_property(self):
        return 15

    def method_without_property_2(self, v):
        return v

l = DataSet()
print(l.method_with_property)
print(l.method_without_property())
print(l.method_without_property_2(14))


#与所定义的属性配合使用，这样可以防止属性被修改
#python属性定义，无法设置私有属性，通过@property的方法来进行社会
#这样可以隐藏属性名，让用户进行使用的时候无法随意修改

class DataSet(object):
    def __init__(self):
        self._images = 1
        self._labels = 2  #定义属性的名称

    @property
    # 方法加入@property后，这个方法相当于一个属性，
    # 这个属性可以让用户进行使用，而且用户没有办法随意修改
    def images(self):
        return self._images

    @property
    def labels(self):
        return self._labels

l = DataSet()
#用户进行属性调用，直接调用images方法即可，不知道属性名_images
#因此用户无法更改属性，从而保护了类的属性
print(l.images)  #加了@property之后，可以用调用属性的形式来调用方法，后面不需要加（）