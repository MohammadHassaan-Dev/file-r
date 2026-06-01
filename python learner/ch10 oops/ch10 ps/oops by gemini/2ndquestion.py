class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print(f"{self.name} got {self.marks} marks")

obj = Student("Hassaan", 90)
obj.show()
# Hassaan got 90 marks