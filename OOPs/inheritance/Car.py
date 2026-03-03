class Car:
    def __init__(self):
        self.brandName = "MG"

class Windsor(Car):
    pass

w = Windsor()

# print(w)
print(w.__dict__)

print(Windsor.__mro__)  # (<class '__main__.Windsor'>, <class '__main__.Car'>, <class 'object'>)
# Windsor --> Car --> Object 


# print(w.__class__.__mro__) == print(Windsor.__mro__)   // both are same 
# mro for the method resolution order