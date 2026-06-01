class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show(self):
        print(f"{self.brand} speed is {self.speed}")

car1 = Car("Toyota", 180)
car2 = Car("Honda", 200)

car1.show()
car2.show()

Car.show(car1)