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