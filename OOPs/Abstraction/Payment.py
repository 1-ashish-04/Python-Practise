from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod   # Incomplete  method
    def makePayment(self, amount):
        pass

class CreditCardPayment(Payment):

    def makePayment(self, amount):  # complete method
        print(f"PRocessing credit card payment of {amount}")

class UPI(Payment):

    def makePayment(self, amount): # complete method
        print(f"Processing payment of upi {amount}")


c = CreditCardPayment()
c.makePayment(200)

u = UPI()
u.makePayment(100)

p = Payment()  # TypeError: Can't instantiate abstract class Payment without an implementation for abstract method 'makePayment'
