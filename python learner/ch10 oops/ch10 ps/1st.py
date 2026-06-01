# 1. Create a class “Programmer” for storing information of few programmers 
# working at Microsoft.


class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

programmer1 = Programmer("Hassaan", 12000)
programmer2 = Programmer("Ali", 1200000)
print(Programmer.company,programmer1.name, programmer1.salary)
print(Programmer.company,programmer2.name, programmer2.salary)