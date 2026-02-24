class Employee:
    companyName = "DCL"  # class-object space inside heap space, single, copy
    code = 59062
    
    def __init__(self):
        self.empId = None #instance variable
        self.empName = None   #instance variable

print("***Invoked from class object***", Employee.companyName) #class object
e1 = Employee()              
print("***Invoked from class object***",e1.companyName)

e1.companyName = "Google"
print("***Invoked from object***                                                                 9i99999999999999999999999999999999999999999999999999999999999999999999999999999", e1.companyName)
print(Employee.companyName)

e1.salary = 1000000 # creating instance variable using object reference  #second method
print(e1.salary)

# print(e1.companyName) # not recomended , as it is a time consuming and unnecessary
print(Employee.companyName) # recommend way  
    
print(Employee.__dict__) # display the dictionary of class Employee

print(e1.__dict__) # display the dictionary of e1 object
