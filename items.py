import random

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.is_equipped = False  # Optional flag for equip logic

    def inspect(self):
        print(f"{self.name} - {self.description}")

    def equip(self):
        self.is_equipped = True
        print(f"{self.name} is now equipped for.")

    def use(self, character):
        if self.name in ['axe', 'flashlight', 'bow']:
            damage = random.randint(45, 100)
            print(f"{character.name} uses {self.name} and deals {damage} damage!")
            return damage  # You can use this to apply damage to a monster
        elif self.name == 'beer':
            character.get_heal(25)
            print(f"{character.name} uses {self.name} and healed 25 hp!")
        elif self.name == 'potion':
            character.get_heal(75)
        elif self.name == 'bear trap':
            print(f"{character.name} sets a trap... It will spring on the next enemy!")
        else:
            print(f"{self.name} has no effect right now.")

