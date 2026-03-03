class Car:

    def assignBrand(self):
        self.brand = "MG"


class Windsor(Car):

    pass

w = Windsor()
print("Before", w.__dict__)  # {}
w.assignBrand()  #These step create the instance variable into the Windsor class from Car class
print("After", w.__dict__) # {'brand': 'MG'}