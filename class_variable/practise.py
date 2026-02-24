class Dcl:
    deptName = "SoftwareDeveloper" # class variable
    def __init__ (self):
        self.empId = None #instance variable

d1 = Dcl()

print(Dcl.__dict__)

print(d1.__dict__)

print(d1.deptName) #not recommended to access the class variable using object reference

d1.deptName = "HR"


print(Dcl.__dict__)

print(d1.__dict__)

print(d1.deptName)
print("****************************************************************************")
d2 = Dcl()
print(d2.deptName)
print(d1.deptName)
print(d2.__dict__)