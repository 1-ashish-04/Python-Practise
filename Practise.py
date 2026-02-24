class Practise:
    companyName = "DheeCodingLab"  # class variable

    def __init__(self):
        self.empName = None #instance vairable
        self.empId = None
    
    def verifyStuent(func_name):  #decorator
        def wrapp9er_name(self):
            print("Verrifying sudent background")
            func_name(self)
            print("Successfully enrolled!!!")
        return wrapp9er_name

    @verifyStuent
    def studentEnroll(self): # instance method with decorator wrapper
        print("Student enrolled in particular course.")

p = Practise() 

p.studentEnroll() # instance method is invoked