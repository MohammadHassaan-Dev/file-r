class Car:
    def __init__(self, car):
        self.__car = car

    def get_car(self):
        return self.__car
    def goodday(self):
        return "Hy!"
    
class ElectricCar(Car):
    def __init__(self, car, battery_type):
        super().__init__(car)
        self.battery_type = battery_type

car1 = ElectricCar("Tesla", "lithium")
print(car1.get_car(), car1.battery_type, car1.goodday())
# print(car1.goodday())