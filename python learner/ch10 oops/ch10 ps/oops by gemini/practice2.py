class Car:
    def __init__(self, car):
        self.car = car

    def goodday(self):
        return "Hy!"
    
class ElectricCar(Car):
    def __init__(self, car, battery_type):
        super().__init__(car)
        self.battery_type = battery_type

car1 = ElectricCar("Tesla", "lithium")
print(car1.car, car1.battery_type, car1.goodday())