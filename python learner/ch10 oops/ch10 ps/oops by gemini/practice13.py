class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show(self):
        print(self.brand)

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def details(self):
        print(self.brand, self.model)

car1 = Car("BMW", 'M5')
car1.show()
car1.details()