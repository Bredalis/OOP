
from abc import ABC, abstractmethod


class Character(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name
        self.level = 0
        self.inventory = []
        self.health = 100

    @abstractmethod
    def attack(self, target):
        pass

    @abstractmethod
    def status(self):
        print(f"Name: {self.name}\nLevel: {self.level}")

    def level_up(self):
        self.level += 1

    def get_inventory(self):
        print(f"Inventory of: {self.name}")
        for item in self.inventory:
            print(item)


class Wizard(Character):
    def __init__(self, name):
        super().__init__(name)
        self.health = 120
        self.intelligence = 95
        self.inventory = ["Mana Potion", "Grimoire"]

    def status(self):
        print("Class: Wizard")
        super().status()

    def attack(self, target):
        target.health -= self.intelligence * 0.6
        print(f"Target's current health is: {target.health}")


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name)
        self.health = 200
        self.strength = 75
        self.inventory = ["Health Potion", "Shield", "Sword"]

    def status(self):
        print("Class: Warrior")
        super().status()

    def attack(self, target):
        target.health -= self.strength * 0.8
        print(f"The target has {target.health} health points remaining")


warrior = Warrior("Pedro")
wizard = Wizard("Yuto")

characters = [warrior, wizard]

for character in characters:
    character.status()
    character.get_inventory()
    character.attack(character)
