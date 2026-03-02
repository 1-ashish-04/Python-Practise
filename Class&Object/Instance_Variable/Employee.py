class Employee:
    def __init__(self):
        self.employeeId = 101
        self.employeeName = 'Ashish'

e = Employee()
print(e)
print(e.employeeId, e.employeeName)


 print(Employee.__dict__) # It print the dictionary of the Employee class
print(e.__dict__) # It print the dictionary of the  object
