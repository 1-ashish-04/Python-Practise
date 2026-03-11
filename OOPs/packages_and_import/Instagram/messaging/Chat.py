import login.SignIn as s  # importing complete SignIn class from login

class Chat:

    sign = s.SignIn("Kat", "Kat12345")  # creating the object of SignIn class  # it is a Class Variable (Global Variable)

    def sendMessage(self, message):
        
        Chat.sign.sign_In()  # Calling the SignIn class method --> sign_In(self)   # accessing class variable

        print("Sending message:", message)


    def displayUserName(self):
        print("Displaying user name in chat", Chat.sign.username) # class variable accessing.

c = Chat()
c.sendMessage("Hello, How are you?")
c.displayUserName()