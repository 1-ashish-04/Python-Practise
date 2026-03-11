import authentication.Login as l   # importing everything from Login.py 

class OrderService:

    def place_order(Self, userName):

        loginService = l.LoginService()  # object of LoginService()

        if loginService.authenticate(userName, "1234"):
            print("Order placed successfuly")
            
        else:
            print("Failed to place order! Authentication is invalid.")