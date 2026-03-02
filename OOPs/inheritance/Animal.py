class Animal:
    zoo = "City Zoo" # class variable is inherited

    def __init__(self):
        self.species = "Mammal" # instance variable is inherited

    def sleep(self): # instance method is inherited
        print("Animal is sleeping.")
    
    @classmethod
    def eat(cls): # class method is inherited
        print("Animal is eating")

    @staticmethod
    def dance(): # static method is inherited
        song_name = "123" # statice variable is not inherited, as they are local stored inside the stack (Temporary memory)
        print("Animal is dancing")
    

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

dog1 = Dog() # Object creation (Instantiation)
dog1.bark()

# instance variable and method
dog1.sleep()  
print(dog1.species)

# class variable and method
Dog.eat()
print(Dog.zoo)

# static method
Dog.dance()