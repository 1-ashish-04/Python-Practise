# Multi-Level inheritance

class Animal: #Super class for Dog , and super most class for BabyDog
    def eat(Self):
        print("Animal is eat")

class Dog(Animal): #Super Class for BabyDog, and sub class of Animal
    def bark(self):
        print("Dog is barking")

class BabyDog(Dog): # sub class of Dog
    def weep(self):
        print("Baby Dog is weeping")

# MRO ----> BabyDog --> Dog --> Animal --> Object

print("**********Baby Dog Object*********")
b = BabyDog()
b.weep()
b.bark()
b.eat()

print("**********Dog Object*********")
d = Dog()
d.bark()
d.eat()

print("**********Animal Object*********")
a = Animal()
a.eat()