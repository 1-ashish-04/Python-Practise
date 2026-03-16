class ATM:

    def __init__(self):
        self.__balance = 1000; # Private variable are directly accessible inside only the class, not the outside, for the outside we have to use name mangling

    def getBalance(self):
        return self.__balance
    
    def deposit(self , amount):

        if amount > 0:
            self.__balance += amount
            print("Deposit successful. Current balance: ", self.getBalance()) 

        else:
            print("Invalid Transaction")
        
    def withDrawl(self, amount):

        if amount >= 0 and amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawl successful. Current balance: ", self.getBalance())

        else:
            print("Invalid transaction")

a = ATM()

print("****Initial Balance****")
print(a.getBalance())

print("****Deposit Balance****")
a.deposit(800)

print("***Withdrawl Balance****")
a.withDrawl(200)

# here we indirectly accessing the private vaiable. using the method declared inside the class which present where the private variable declared.