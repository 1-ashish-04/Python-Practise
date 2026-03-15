class Animal:
    def makeSound(self):
        print("All animal make sound")

class Dog(Animal):
    def makeSound(self): # method override
        print("Bow Bow")

animal = Animal()
animal.makeSound()

dog = Dog()
dog.makeSound()

print(dog.makeSound.__func__ == animal.makeSound.__func__) # it check both methd declaration and method body if both same then give the True otherwise False (It is used to check in method Overriding)
