class Car:

    def __init__(self):
        self.model = 2025

    def assignBrand(self):
        self.brand = "MG"


class Windsor(Car):

    def __init__(self):
        self.engineCountry = "British"

w = Windsor()
print("Before", w.__dict__)  # Before {'engineCountry': 'British'}
w.assignBrand()
print("After", w.__dict__) # After {'engineCountry': 'British', 'brand': 'MG'} 