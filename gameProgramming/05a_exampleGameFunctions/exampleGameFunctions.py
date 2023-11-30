# Example Game Functions Project, Noah Mulder, v7
import random

player_hp = 100
cpu_hp = 100
player_name = ""
cpu_name = ""
attack_potency = 0.0 # Max attack potency is 5
elemental_attack = None # Elemenatl attacks are Fire, Ice, Lightning
cpu_namelist = ["Rodrick", "Grag", "Tyu", "Boder", "Poly"]
attack_type = ""

player_name = input("What is your characters name?\n")

def get_cpuname(cpu_namelist):
    name_index = random.randint(0, len(cpu_namelist) - 1)
    cpu_name = name_index
    return(cpu_name)

def function_three(param1 = "Default Value"):
    pass

def elemental_damage(elemental_attackchosen, elemental_bonus):
    elemental_attackchosen = input("What element would you like to use? Fire, Ice, or Lightning?\n")
    elemental_attackchosen = ["Fire", "Ice", "Lightning"]
    if "Fire":
        health_taken = 10 * (attack_potency) + (elemental_bonus)
    elif "Ice":
        health_taken = 10 * (attack_potency) + (elemental_bonus)
    elif "Lightning":
        health_taken = 10 * (attack_potency) + (elemental_bonus)
    else:
        print("You didn't choose a valid elemental attack.")
pass

while player_hp or cpu_hp != 0:
    print(f"{player_name} HP: {player_hp}\n")
    print(f"{cpu_name} HP: {cpu_hp}\n")
    attack_type = input("What type of attack would you like to use? Light or Heavy?\n")
    if "light" or "Light":
        attack_potency = random.randint(1.0, 5.0)
        #print(attack_potency)
        health_taken = 5 * (attack_potency)
        cpu_hp -= health_taken
    elif "heavy" or "Heavy":
        attack_potency = random.randint(1.0, 5.0)
        #print(attack_potency)
        health_taken = 10 * (attack_potency)
        cpu_hp -= health_taken
    else:
        print("Choose of the two attack types.")

def play_again():
    print('Do you want to fight again? Yes or No?\n')
    return input().lower().startswith('y')