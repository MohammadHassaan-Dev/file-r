# 2. Write a class “Calculator” capable of finding square, cube and square root of a 
# number.

class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"Square of {self.n} = {self.n * self.n}")

    def cube(self):
        print(f"Cube of {self.n} = {self.n * self.n * self.n}")

    def square_root(self):
        print(f"SquareRoot of {self.n} = {self.n ** 0.5}")

calc = Calculator(2)
calc.square()
calc.cube()
calc.square_root()