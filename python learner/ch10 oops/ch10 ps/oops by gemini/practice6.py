class GamePlayer:
    def __init__(self, health):
        self.__health = health

    def damage(self, amount):
        self.__health -= amount

    def show_health(self):
        return self.__health
    
Gameplayer1 = GamePlayer(100)
Gameplayer1.damage(30)
print(Gameplayer1.show_health())