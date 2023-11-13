# Example Game Functions Project, Noah Mulder, v2
import random

player_hp = 100
cpu_hp = 100
player_name = ""
cpu_name = ""
attack_potency = 0.0
elemental_attack = False
cpu_namelist = ["Rodrick", "Grag", "Tyu", "Boder", "Poly"]

def function_one():
    pass

def get_cpuname(cpu_namelist):
    name_index = random.randint(0, len(cpu_namelist) - 1)
    print(name_index)

def function_three(param1 = "Default Value"):
    pass

def function_four(param1, param2):
    pass