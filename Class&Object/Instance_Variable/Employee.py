class Employee:
    def __init__(self):
        self.employeeId = 101 # Instance Variable
        self.employeeName = 'Ashish' # Instance Variable

e = Employee()
print(e)
print(e.employeeId, e.employeeName) # Instance Variable calling using object reference


print(Employee.__dict__) # It print the dictionary of the Employee class
print(e.__dict__) # It print the dictionary of the  object
