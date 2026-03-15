import Folder1.A as a

class B(a.A):

    def printData(self):
        # a1 = a.A()
        # print(a1.x)
        # print(a1._y)
        # print(a1.__dict__)  # {'x': 10, '_y': 20}
        pass
    
b = B()
print(b._y)
print(b.__dict__)