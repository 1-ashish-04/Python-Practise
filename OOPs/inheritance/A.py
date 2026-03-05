# Hybrid Inheritance


#    A
#   / \
#  B   C
#   \ /
#    D

class A:
    def display(self):
        print("Displaying")
    

class B(A):
    def run(self):
        print("run")

class C(A):
    def runner(self):
        print("Runner")

class D(B,C):
    pass

print("D Object")
d = D()
d.runner()
d.run()
d.display()

print("C Object")
c = C()
c.runner()
c.display()

print("B Object")
b = B()
b.run()
b.display()

print("A Object")
a = A()
a.display()