
from random import randint


class SlotMachine:
    def __init__(self, machine_id, prize):
        self.machine_id = machine_id
        self.prize = prize
        self.coins = 0
        self.jackpots = 0

    def __str__(self):
        return f"id: {self.machine_id} - prize: {self.prize}"

    def __eq__(self, other):
        return self.coins == other.coins

    def __lt__(self, other):
        return self.coins < other.coins

    def __gt__(self, other):
        return self.coins > other.coins

    def play(self):
        self.coins += 1
        numbers = (randint(0, 9), randint(0, 9), randint(0, 9))

        if numbers[0] == numbers[1] == numbers[2]:
            self.jackpots += 1
            message = f"You won {self.prize}"
        else:
            message = "Better luck next time"

        return numbers, message


player_1 = SlotMachine("1", "20000$")
player_2 = SlotMachine("1", "20000$")

print(player_1)
print(player_1.machine_id == player_2.machine_id)

for i in range(100):
    print(player_1.play(), i)
