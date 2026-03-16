class Student:

    def __init__(self):
        self.stuId = 101 # public
        self.__stuMarks = 59  #Private

    def getStuMarks(self):
        return self.__stuMarks
    
    def setStuMarks(self, marks):
        if marks >= 0  and marks <= 100:
            self.__stuMarks = marks
            print("Marks updated successfully. current marks: ", self.getStuMarks())
        else:
            print("Invalid marks")
        
class Teacher:

    # Pass by reference   ---> address of the student object is passed as an input parameter into another function
    def modifyMarks(self, studentObjAdd, marks):
        studentObjAdd.setStuMarks(marks)   # s.setStuMarks(marks)

s = Student()
print("****Initial Marks****")
print(s.getStuMarks())

print("****Modify marks****")

t = Teacher()
t.modifyMarks(s, 90)