# Multiple Inheritance
class Father:
    def drive(self):
        print("Faher knows how to drive")

class Mother:
    def drive(self):
        print("Mother knows how to drive")

    def cook(self):
        print("Mother knows how to cook")

class Son(Mother, Father):
    def play(self):
        print("Knows how to play")

class Daughter(Father, Mother):
    def read(self):
        print("Knows how to read")

# by MRO known as C3 algorithm
# firstly it check the properties in left most class, then goes to the right most class (in multiple inheritance)

s = Son()  # Mother , Father
s.play()
s.drive() # Mother knows how to drive
s.cook() # Mother knows how to cook 

d= Daughter()  # Father, Mother
d.read()
d.drive() # Faher knows how to drive 
d.cook() # Mother knows how to cook 