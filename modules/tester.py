import dice

roll1 = dice.roll(1, 6)
roll2 = dice.display(1, 6)


if dice.is_exploding(roll1, 6):
    print(roll1)
    print("This roll exploded!\n")
    roll1 += dice.roll(1, 6)
    print(roll1)

    