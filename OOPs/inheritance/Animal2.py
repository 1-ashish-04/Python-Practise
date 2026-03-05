# Hierarchial inheritance

class Animal: 
    def eat(Self):
        print("Animal is eat")

class Dog(Animal): 
    def bark(self):
        print("Dog is barking")

class Cat(Animal): 
    def meow(self):
        print("Cat is meowing")
    
class Lion(Animal):
    def roar(self):
        print("Lion is roaring")


print("**********Dog Object*********")
d = Dog()
d.bark()
d.eat()

print("**********Cat Object*********")
c = Cat()
c.meow()
c.eat()

print("**********Lion Object*********")
l = Lion()
l.roar()
l.eat()

print("**********Animal Object*********")
a = Animal()
a.eat()