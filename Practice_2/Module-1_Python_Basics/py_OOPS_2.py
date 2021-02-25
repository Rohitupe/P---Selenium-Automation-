# Constructor and its role in object

class Calculator:
    # class level variable
    __class_variable = "This is classs variable"

    def __init__(self, first_name, last_name):  # constructor in python
        print("constructor called")

        # instance level variable
        self.fName = first_name
        self.lName = last_name

    def fullName(self, age):
        print("function called")
        print(self.fName + " " + self.lName + " and age is " + str(age))


obj1 = Calculator("Rohit", "Tupe")
obj1.fullName("23")
