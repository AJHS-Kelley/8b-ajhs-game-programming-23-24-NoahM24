import dice

roll1 = dice.roll(1, 6)
roll2 = dice.display(1, 6)

if dice.is_doubles(roll1, roll2):
    print("You rolled a double, go again!\n")
else:
    print("It was not a double.\n")