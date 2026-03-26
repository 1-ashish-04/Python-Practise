class BookMyShow:

    def makePayment(self): # instance method
        print("Payment is successfull.")

b = BookMyShow()
# print(b)   # <__main__.BookMyShow object at 0x000001B059068830>
print(b.__dict__) # {}

b.makePayment() # Payment is successfull.

print(b.__class__) #<class '__main__.BookMyShow'>

print(b.__class__.__dict__) # {'__module__': '__main__', '__firstlineno__': 1, 'makePayment': <function BookMyShow.makePayment at 0x0000018B878B7530>, '__static_attributes__': (), '__dict__': <attribute '__dict__' of 'BookMyShow' objects>, '__weakref__': <attribute '__weakref__' of 'BookMyShow' objects>, '__doc__': None}


print(b.__class__.__dict__['makePayment']) #<function BookMyShow.makePayment at 0x00000282FDC67530>