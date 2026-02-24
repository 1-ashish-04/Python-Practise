class DecoratorTest:

    def verifyUser(func_name): # decorator

        def wrapper_name(self): # wrapper function  ------> # in new update, need to pass the self keyword as parameter when applying the decorator into the instance method.                                                                                            

            print("Verifying the User...")

            func_name(self) # in new update, need to pass the self keyword as parameter when applying the decorator into the instance method.

            print("User has completed the operation, logged out successfully.")

        return wrapper_name

    @verifyUser # decorator name
    def startTest(self):
        print("Student started the test.")

    @verifyUser # decorator name
    def applyForHallticket(self):
        print("Student applied for the hall ticket.")

d = DecoratorTest()

d.applyForHallticket()

d.startTest()