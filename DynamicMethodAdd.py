'''Dynamic Method Addition to Classes and Instances'''

from types import MethodType

class MyObj(object):
    def __init__(self, value):
        self.val = value

def new_method(self, value):
    return self.val + value

obj = MyObj(3)
obj.method = new_method
##obj.method(5) # TypeError
print(obj.method, 'TypeError: Missing self')

obj.method = MethodType(new_method, obj)
print(obj.method(5))

MyObj.method = new_method
obj2 = MyObj(2)
print(obj2.method)
print(obj2.method(5))

obj.foo = MethodType(lambda self: 42, obj)
print(obj.foo)
print(obj.foo())
