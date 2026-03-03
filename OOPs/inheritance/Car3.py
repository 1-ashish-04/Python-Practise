class Car:

    def __init__(self):  # for Car
        self.model = 2025

    def assignBrand(self): # instance method inside Car class
        self.brand = "MG"


class Windsor(Car):

    def __init__(self): # for Windsor
        self.engineCountry = "British"

w = Windsor()
print("Before", w.__dict__)  # Before {'engineCountry': 'British'}

w.assignBrand() # through MRO, Windsor object access the instance method define inside the Car class,
# in it firstly check the Windsor class, if not find go to the Car class, then executing these,, then only the brand = "MG", is created inside the Windsor Object

print("After", w.__dict__) # After {'engineCountry': 'British', 'brand': 'MG'} 