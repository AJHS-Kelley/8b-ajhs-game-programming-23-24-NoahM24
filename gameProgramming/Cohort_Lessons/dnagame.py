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