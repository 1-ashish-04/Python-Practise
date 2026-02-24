class Student:
    def __init__(self):
        self.studentId = None
        self.studentName = None
    
s1 = Student() #Instantiation
print("*******BEFORE VARIABLE INITIALIZATION (DATA ASSIGN)")
print(s1.studentId)
print(s1.studentName)

print("*******AFTER VARIABLE INITIALIZATION (DATA ASSIGN)")
s1.studentId = 808  # initialization
s1.studentName = 'Ashish' # initialization
print(s1.studentId)
print(s1.studentName)