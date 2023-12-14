# Dice Rolling Module, Noah Mulder, v1
import random

def roll_dice(num_dice, size_dice):
    num_rolled = 0
    sum = 0
    while num_rolled < num_dice:
        roll = random.randint(1, size_dice)
        sum += roll
        print(f"Roll: {roll}\n")
        print(f"Sum: {sum}\n")
        num_rolled += 1
    return sum