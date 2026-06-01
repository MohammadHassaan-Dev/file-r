class Gamer:
    game = "Minecraft"
    @classmethod
    def show(cls):
        print(f"the class attribute is {cls.game}")

a = Gamer()
a.game = "FreeFire"
a.show()