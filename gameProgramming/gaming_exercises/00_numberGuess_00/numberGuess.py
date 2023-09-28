# Select the secret number from a given range.
# Player must guess the number.
# Compare guess to the secret number.
# What happens if the guess is wrong?
    # Tell them the guess is wrong. 
    # Tell them the number of guess left.
    # Tell them if too high / too low.
# What happans if the guess is right?
    # Tell them guess is correct
    # Award a point
# What happens if the player runs out of guesses?
    # Tell player round has been lost.
    # Award point to CPU.
# Check to see if player or CPU had >= 3 points, if so they win.
# Easy is 5 guesses with range of 20
# Medium has 4 guesses with range of 35
# Hard has 3 guesses with range of 50

import random # Import the random module to our code.
import time 
# All code works as expected, well done! 
#DECLARATIONS
secret_number = -1
player_guess = -1
player_score = 0
cpu_score = 0
num_guesses = 0
player_name = ""
difficulty = ""
range_min = -1
range_max = -1
num_attempts = -1

print("""
        *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
        |                             |  
        |         Guess Number        |
        |          Noah Mulder        |
        |            2023             |
        |                             |
        *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
    """)

# CPU SECRET NIMBER GENERATOR


# GAME LOOP
print("You need to guess a number from 0 to 20 and you have 4 guesses.\nIf you guess it right, you get a point.\nIf you don't get it in 4 guesses, the cpu gets a point.")
# Use input() to store difficulty in difficulty varible
# assign values to num_attempts, range_min, and range_max based on choice
print("Easy has a range of 20 with 5 guesses.\nMedium has a range of 35 with 4 guesses.\nHard has a range of 50 with 3 guesses.\nImpossible is just like Hard but with ONE guess.\nHelp Me is a fun difficulty of on guess between 0 and 10.\n")

while player_score != 3 and cpu_score != 3: # Starts the match (game)
    # pass -- Tells Python to skip this block of code    
    print(f"Player Score: {player_score}\nCPU Score: {cpu_score}.\n")
    
    # Whenever you assign a specific value to something, it's called "hard coded".
    difficulty = input("Choose a difficulty.")
    # Add the code to actually select the difficulty.  
    # print(secret_number)
    if difficulty == "Easy":
        num_attempts = 5
        range_min = 0
        range_max = 20
    elif difficulty == "Medium":
        num_attempts = 5
        range_min = 0
        range_max = 35
    elif difficulty == "Hard":
        num_attempts = 3
        range_min = 0
        range_max = 50
    elif difficulty == "Impossible":
        num_attempts = 1
        range_min = 0
        range_max = 50
    elif difficulty == "Help Me":
        num_attempts = 1
        range_min = 0
        range_max = 10
    else:
        print("Negative. Choose Again.")
    secret_number = random.randint(range_min, range_max)
   
    num_guesses = 0
    for guesses in range(num_attempts): # Starts the round
        
        print(f"You have {num_attempts - num_guesses} guesses remaining.\n")
        player_guess = int(input(f"Type a number from {range_min} to {range_max} and press ENTER.\n"))
        # input() saves all data as a STRING by default
        # int() will convert to an INTEGER
        # float() will convert to a FLOAT
        print(f"You have chosen {player_guess}. Let's see if you're right!\n")
        if player_guess == secret_number:
            print("You got it right! =)\n")
            player_score += 1
            break # IMMEDIATELY EXIT ANY LOOP YOU ARE IN!
        else:
            print("You got it wrong. =(\n")
            if player_guess > secret_number:
                print("Your guess is too high.\n")
            else:
                print("Your guess is too low.\n")
        num_guesses += 1
    if player_guess != secret_number:
        cpu_score += 1
        print("CPU gets the point. Guess better.\n")
if player_score >= 3:
    print("You win. Good job\n")
else:
    print("Imagine losing to a computer. That's cringe.\n")