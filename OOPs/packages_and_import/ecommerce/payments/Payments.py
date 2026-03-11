from authentication.Login import LoginService

class PaymentService:

    def make_payment(self, userName, amount):
        loginService = LoginService() # object of class LoginService
        
        if loginService.authenticate(userName, "1234"):
            print(f"Payment of {amount} Rupee made successfully")

        else:
            print("Failed to make an payment! authentication not successfully.")