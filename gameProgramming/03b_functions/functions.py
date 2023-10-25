# 8B 03_functions Mulder_Noah 10/25/2023 v0.3
import random
# FUNCTIONS -- a named piece of code that can be reused easily
# FUNCTION SIGNATURE -- Syntax for creating a new function.
# def example_functionA(): # NO PARAMETERS
#     count = 0
#     num = int(input("How many times do you want to wish a happy birthday?\n"))
#     while count < num:
#         print("Happy Birthday!\n")
#         count += 1

# def example_functionB(num, count): # PARAMETERS
#     while count < num:
#         print("Happy Birthday!\n")
#         count += 1

# IF A FUNCTION REQUIRES PARAMETERS, YOUR CODE WILL CRASH WITHOUT THEM!

# RUNNING A FUNCTION IS KNOWN AS CALLING THE FUNCTION
# example_functionA()
#example_functionB(5, 0)

def roll_dice(num_dice, size_dice):
    num_rolled = 0
    sum = 0
    while num_rolled < num_dice:
        roll = random.randint(1, size_dice)
        sum += roll
        print(f"Roll: {roll}\n")
        print(f"Sum: {sum}\n")
        num_rolled += 1
    return sum  # return will IMMEDIATELY exut a loop, function, if/elif/else block

# roll_dice(4, 9)
# roll_dice(2, 20)
# roll_dice(1, 200)

strength_player = roll_dice(3, 6)
dexterity_player = roll_dice(3, 6)
wisdom_player = roll_dice(3, 6)

print(strength_player)
print(dexterity_player)
print(wisdom_player)

def gen_stats():
    player_stats = [
        0, #STR
        0, #DEX
        0, #CON
        0, #INT
        0, #WIS
        0  #CHA
    ]
    i = 0
    while i < len(player_stats):
        player_stats[i] = roll_dice(3, 6) # STRENGTH
        i += 1
    
    
    print(player_stats)

gen_stats()