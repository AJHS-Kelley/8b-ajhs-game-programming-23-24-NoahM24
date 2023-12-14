# Dice Rolling Module, Noah Mulder, v2
import random

def roll(num_dice, size_dice): # Works
    num_rolled = 0
    sum = 0
    while num_rolled < num_dice:
        roll = random.randint(1, size_dice)
        sum += roll
        num_rolled += 1
    return sum

def display(num_dice, size_dice): # Works
    num_rolled = 0
    sum = 0
    while num_rolled < num_dice:
        roll = random.randint(1, size_dice)
        sum += roll
        print(f"Roll: {roll}\n")
        print(f"Sum: {sum}\n")
        num_rolled += 1
    return sum

def is_doubles(roll1, roll2):
    if roll1 == roll2:
        is_doubles = True
    else:
        is_doubles = False
    return is_doubles

def is_exploding(roll, size_dice):
    if roll == size_dice:
        is_exploding = True
    else:
        is_exploding = False
    return is_exploding