# Multiple Inheritance
class Father:
    def drive(self):
        print("Knows how to drive")

class Mother:
    def cook(self):
        print("Knows how to cook")

class Son(Father,Mother):
    def play(self):
        print("Knows how to play")

s = Son()
s.play()
s.drive()
s.cook()