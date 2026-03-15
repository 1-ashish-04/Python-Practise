class Calculate:

    '''def add(self): # this method removed
        x = 10
        y = 20
        z = x + y

    def add(self, a , b): # this method removed
        return a + b

    def add(Self, x , y): # this method get executed
        a = x
        b = y 
        c = a + b
        print("Add method with x and y params")'''

    def __init__(self):  # removed 
        
        print("Constructor without params")

    def __init__(self, a, b): # these will get executed
        print("Constructor with params")
        self.x = 2
        self.y = 4
        self.z = self.x + self.y

c1  = Calculate(1,2)
