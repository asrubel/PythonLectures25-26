from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name, rank, level):
        self.name = name
        self.rank = rank
        self.level = level

    @abstractmethod
    def fight(self):
        ...

    @abstractmethod
    def spell(self):
        ...

    def sing(self):
        print(f"I am {self.name}! And I don't sing!")


class Warrior(Player):
    def fight(self):
        print("Swing a sword...")

    def spell(self):
        print("Heal wounds...")


class Witcher(Player):
    def fight(self):
        print("Throw a fireball...")

    def spell(self):
        print("Cast a spell...")


# player = Player(name='<NAME>', rank=1, level=1)
warrior = Warrior("John", 1, 10)
warrior.fight()
warrior.spell()
warrior.sing()

witcher = Witcher("Gerald", 2, 20)
witcher.fight()
witcher.spell()
witcher.sing()
