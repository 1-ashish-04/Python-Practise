import login.SignIn as s # importing everything present in SignIn.py from login folder

from login.SignIn import SignIn;

class Reels:

    def createReels(self, content):

        # sign = s.SignIn("Jonh", "Pass1234")  # creating the object of SignIn class  (Local variable) ---> if using import login.SignIn as s

        sign = SignIn("Jonh", "Pass1234")  # creating the object of SignIn class  (Local variable)

        sign.sign_In() # Calling the SignIn class method --> sign_In(self)
        
        print("Creating a new reel with content:", content)

    def shareReels(self, reel_id):
        #SignIn
        print("Sharing a reel with reel ID:", reel_id)


reel = Reels()
reel.createReels("My new reels")
reel.shareReels("3565")