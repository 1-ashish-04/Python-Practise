class LoginService:

    def authenticate(self, userName, pasword):
        if userName == "Admin" and pasword == "1234":
            print("Login successful!")
            return True
        
        print("Failed to login, invalid username or password")
        return False