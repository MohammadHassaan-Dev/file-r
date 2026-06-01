class Cat:
    def speak(self):
        print("Meow")


class Dog:
    def speak(self):
        print("Bark")


class Cow:
    def speak(self):
        print("Moo")

animals = [Cat(), Dog(), Cow()]

for animal in animals:
    animal.speak()