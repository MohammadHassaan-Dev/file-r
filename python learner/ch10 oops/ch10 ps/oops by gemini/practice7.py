class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"
    
class Cat(Animal):
    pass

cat1 = Cat("Tom")
print(cat1.speak())