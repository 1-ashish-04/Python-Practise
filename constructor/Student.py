class Student:

    # instantiate  of the object done by __new__(cls)

    def __init__(self):  # object initialization is done here
        self.id = 101
        self.name = "John"

s1 = Student()  # 1... PVM read these line, goes to the class search for __new__(cls)  (constructor) 2... if not find go to the Object class,  3... call the constructor and  4..  memory allocate to the object (known as instantiate), 5... then PVM take address from there give it to the __init__(self) method,  6... then __init__(self) initialize the variable.