class BookMyShow:

    # instance method with pass by parameter -----------------------------------------


    def makePayment(self, paymentType):
        print(paymentType, "Payment is successfull.")

    def makePayment2(self, paymentType):
        self.type = paymentType   # these instance variable is global can easily accessible outside of these method.

        print(self.type, "Payment is successfull.")


b1 = BookMyShow()
b1.makePayment("Cash") 

print(b1.__dict__) # {}

b1.makePayment2("Card")

print(b1.__dict__) # {'type': 'Card'}

b1.type = "Internet Banking"
print(b1.__dict__) #{'type': 'Internet Banking'}
print(b1.type) #Internet Banking


b1.makePayment2(b1.type) # it like a extra headache, as the instance variable already assign the value 'Intenet Banking' using these we reassign the value to same instance variable, just now invoking the makePayemnt2 method.



