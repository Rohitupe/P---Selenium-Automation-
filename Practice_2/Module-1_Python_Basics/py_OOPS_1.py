# Creating simple class in python

class Calculator:
    # class level variable
    var = 100

    def home(self):
        print("hello world")


obj = Calculator()  # syntax to create object
print(obj.var)
obj.home()
