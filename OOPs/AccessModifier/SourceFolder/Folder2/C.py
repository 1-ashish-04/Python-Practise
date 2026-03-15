import Folder1.A as a


class C:
    def display(self):
        a2 = a.A()
        print(a2.x)
        print(a2._y)
        print(a2.__dict__)  # {'x': 10, '_y': 20}

c = C()
c.display()