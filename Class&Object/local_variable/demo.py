class Employee:

    def __init__(self):
        salary = 100000 # Local Variable
        print(salary)

        print("END")
    print("Can not accessible outside init.")
print("can not accessible outside class")

e1 = Employee() # object reference   #objecname and class name should be same
