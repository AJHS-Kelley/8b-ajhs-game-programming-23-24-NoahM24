# DNA Replication Game, Noah Mulder, v1

# Import Entire Modules -- Get the whole tool box.
import time, datetime

# Import Specific Methods -- Get the specific tool.
from random import choice

# Stores the DNA Bases
dna_bases = ["A", "C", "G", "T"]

# GAME FUNCTIONS
def game_intro() -> None:
    pass

def gen_dna() -> str:
    bases_generated = 0
    bases_requested = int(input("Please enter a positive integer number of bases to generate.\n"))
    dna_sequence = ""
    while bases_generated < bases_requested:
        dna_sequence += choice(dna_bases)
        bases_generated += 1
        return dna_sequence
dna = gen_dna()

def do_transcription(dna_sequence: str) -> tuple:
    print(f"The DNA sequence is {dna_sequence}.\n")
    print("You will now generate the RNA sequence that would match.\n")
    print("Please remember, in the RNA sequence U pairs with A from the DNA sequence.\n")
    rna_start = time.time() # time.time() returns the number of seconds since 00:00:00 UTC Jan. 01, 1970
    rna_sequence = input("Please enter the matching RNA sequence. Leave no spaces! Then press enter.\n").upper()
    if rna_sequence not in 'AGCU':
        print("That is not in the RNA sequence. Try again.\n")
    rna_stop = time.time()
    rna_time = rna_stop - rna_start
    return (rna_sequence, rna_time)
# Tuples are ORDERED -- you can reference elements with the index
# Tuples are UNCHANGEABLE -- you cannot add, modify, or delete after creating
# Tuples CAN have duplicates values.

def verify_sequence(dna_sequence: str, rna_sequence : str) -> bool:
    is_match = False
    if len(dna_sequence) != len(rna_sequence):
        print("The amount of bases don't match.\n")
        return is_match
    for dna_base, rna_base in zip(dna_sequence, rna_sequence):
        if dna_base == "A" and rna_base == "U":
            is_match = True
        elif dna_base == "C" and rna_base == "G":
            is_match = True
        elif dna_base == "G" and rna_base == "C":
            is_match = True
        elif dna_base == "T" and rna_base == "A":
            is_match = True
        else:
            print("Not sure if bases match correctly. That's kinda cringe.\n")
    return is_match

def calc_score(rna_sequence: str, rna_time: float) -> int:
    score = 0
    if rna_time < 1.0:
        score += 1000000
    elif rna_time < 5.0:
        score += 900000
    elif rna_time < 10.0:
        score += 600000
    elif rna_time < 15.0:
        score += 450000
    elif rna_time < 20.0:
        score += 300000
    elif rna_time < 30.0:
        score += 200000
    else:
        score += 50000
    
    score_multi = 0.0
    if len(rna_sequence) >= 30:
        score_multi = 5.0
    elif len(rna_sequence) >= 25:
        score_multi = 4.0
    elif len(rna_sequence) >= 20:
        score_multi = 3.0
    elif len(rna_sequence) >= 15:
        score_multi = 2.0
    elif len(rna_sequence) >= 5:
        score_multi = 1.0
    else:
        score_multi = 0.5
    score *= score_multi
    return score

def save_score(dna_sequence: str, rna_sequence: str, rna_time: float, score: int) -> None:
    player_name = input("What is your first name?\n")
    last_name = input("What is your last name?\n")
    full_name = player_name + ' ' + last_name

    file_name = "dna_replicationscore" + full_name + ".txt"
    save_data = open(file_name, "a")
    # File Modes
    # "x" mode -- CREATE FILE, IF FILE EXISTS, EXIT WITH ERROR
    # "w" mode -- CREATE FILE, IF FILE EXISTS, OVERWRITE IT
    # "a" mode -- CREATE FILE, IF FILE EXISTS, APPEND TO IT
    save_data.write(f"DNA Sequence: {dna_sequence}\nRNA Sequence: {rna_sequence}")
    save_data.write(f"Transcription Time: {rna_time}\n")
    save_data.write(f"Score: {score}\n")
    save_data.write(f"{full_name}\n")
    save_data.write(f"{datetime.datetime.now()}\n")
    save_data.close

dna = gen_dna()
rna = do_transcription(dna)
if verify_sequence(dna, rna[0]):
    score = (calc_score(rna[0], rna[1]))
    save_score(dna, rna[0], rna[1], score)