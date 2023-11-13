# Example Game Functions Project, Noah Mulder, v3
import random

player_hp = 100
cpu_hp = 100
player_name = ""
cpu_name = ""
attack_potency = 0.0 # Max attack potency is 5
elemental_attack = None # Elemenatl attacks are Fire, Ice, Lightning
cpu_namelist = ["Rodrick", "Grag", "Tyu", "Boder", "Poly"]

player_name = input("What is your characters name?\n")

print(f"{player_name} HP: {player_hp}\n")
print(f"{cpu_name} HP: {cpu_hp}\n")

def function_one():
    pass

def get_cpuname(cpu_namelist):
    name_index = random.randint(0, len(cpu_namelist) - 1)
    cpu_name = name_index
    print(cpu_name)

def function_three(param1 = "Default Value"):
    pass

def function_four(param1, param2):
    pass

while player_hp or cpu_hp != 0:
    pass