# Hangman Game ny Noah Mulder, v0.3
import random
words = 'Hangman Silver Gold Diamond Platinum Key Keyboard Gorilla Game Program Pow Apple Banana Chloroplast Job Ask Mitochondria Acid Poison Name Help Suffer Watch Lob Lose Corn Cob Same Nine One'.split()

# VARIABLE_NAME in ALL-CAPS ARE CONSTANTS AND NOT MEANT TO CHANGE!
HANGMAN_BOARD = ['''
    +---+
        |
        |
        |       
    ========''','''
    +---+    
    O   |
        |
        |       
    ========''','''
    +---+
    O   |
    |   |
        |       
    ========''','''
    +---+
    O   |
   /|   |
        |       
    ========''','''
    +---+
    O   |
   /|\  |
        |       
    ========''','''
    +---+
    O   |
   /|\  |
   /    |       
    ========''','''
    +---+
    O   |
   /|\  |
   / \  |       
    ========''']

# Pick Word from List
def get_randomword(word_list): # Return a random word from the list.
    word_index = random.randint(0, len(word_list) - 1)
    # len(list_name) - 1 is EXTREMELY COMMON FOR WORKING WITH LISTS.
    return word_list[word_index]

i = 0
while i < 50:
    word = get_randomword(words)
    print(word)
    i += 1