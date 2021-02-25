# inheritance in python

class Parent:
    def __init__(self, father_name, mother_name, surname):
        self.fatherName = father_name
        self.motherName = mother_name
        self.surName = surname

    def fatherFullName(self):
        print(f"{self.fatherName} {self.surName}")

    def motherFullName(self):
        print(f"{self.motherName} {self.surName}")


class Child(Parent):
    def __init__(self, child_name, father_name, surname, mother_name):
        # Parent.__init__(self, father_name, mother_name, surname)
        super().__init__(father_name, mother_name, surname)  # calling all parent methods
        self.childName = child_name

    def childFullName(self):
        print(f"{self.childName} {self.fatherName} {self.surName} {self.motherName}")


child_1 = Child("Rohit", "Dayanand", "Tupe", "Lata")
child_1.childFullName()

child_1.fatherFullName()
child_1.motherFullName()
