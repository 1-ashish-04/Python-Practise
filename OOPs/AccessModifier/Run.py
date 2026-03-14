class Test:

    def __init__(self):
        self.x = 10  # Public variable
        self.__y = 20  # Private Variable

class RunTest:

    def run(self):
        t = Test()
        print("Public variable x:", t.x)
        # print("Private variable y:", t.__y)  # ---> This leads to Attribute Error because __y is a private variable and cannot be accessed directly from outside the class.

        print("Private variable y:", t._Test__y)  # we can access private variable using nameMangling anywhere in the Project
        #  It is a disadvantage in Python, where we can access the Private variable with the nameMangling.

    
r = RunTest()
r.run()

t1 = Test()
print(t1.__dict__)