class Car:
    def __init__(self, brand, fuel):
        self.brand = brand
        self.fuel = fuel

    def drive(self):
        self.fuel -= 20

    def showfuel(self):
        return self.fuel

car1 = Car("BMW", 100)
car1.drive()
print(f"{car1.brand} has {car1.showfuel()} fuel")