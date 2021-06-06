class Descriptor:
    def __init__(self, x):
        self.x = x

    def __get__(self, instance, owner):
        return 0-self.x

    def __set__(self, instance, value):
        self.x = value


class MyClass:
    test = Descriptor(10)

    def my_test(self):
        return (self.test)


m = MyClass()
des = Descriptor(10)
print(m.test)
print(des.x)
print(m.my_test())
m.test = 13
print(m.my_test())