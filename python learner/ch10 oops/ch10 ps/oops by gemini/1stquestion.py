# class Sword:
#     def __init__(self, material, damage):
#         self.material = material
#         self.damage = damage

#     def attack(self):
#         print(f"{self.material} sword attacks with {self.damage} damage")
        
# obj = Sword("diamond", 10)
# obj.attack()
# # Diamond sword attacks with 10 damage

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("toyota", "fortuner")
print(car1.brand, car1.model)