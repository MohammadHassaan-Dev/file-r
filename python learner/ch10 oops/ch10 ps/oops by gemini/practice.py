class Car:
    def __init__(self, name, model):
        self.name = name
        self.model = model
    def hy(self):
        return "HY"
car1 = Car("Toyota", "Corolla")
car2 = Car("Toyota", "Raize")
print(car1.name,car1.model)
print(car2.name,car2.model)
print(car1.hy())
print(car2.hy())