# Hangman Game ny Noah Mulder, v0.5
import random
#words = 'Hangman Silver Gold Diamond Platinum Key Keyboard Gorilla Game Program Pow Apple Banana Chloroplast Job Ask Mitochondria Acid Poison Name Help Suffer Watch Lob Lose Corn Cob Same Nine One'.split()
# DICTIONARY VERSION
# Stored in Key:Value Pairs.
# Actual Dictionary Word (Key) : Value (Definition)
# Uses {} to specify a dictionary.
words = {'Colors': 'red yellow green blue teal silver gold indigo white orange brown pink'.split(),
        'Animals': 'dog cat mouse rat bat monkey bird lion alligator zebra giraffe mule horse'.split(),
        'Shapes': 'square triangle parallelogram circle diamond rhombus octogon pentagon dodecahedron'.split(),
        'Foods': 'hamburger hotdog pizza pasta rice steak chicken fish sushi clams crabs shrimp'.split()}


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

def display_board(missed_letters, correct_letters, secret_word):
    print(HANGMAN_BOARD[len(missed_letters)])
    print()

    print('Missed Letters:', end = ' ')
    for each_letter in missed_letters:
        print(each_letter, end = ' ')
    print()
    
    blanks = '_' * len(secret_word)

    # Replace Blanks with Correct Letters
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]
    
    for letter in blanks:
        print(letter, end = '')
    print()

def get_guess(already_guessed):
    while True:
        print('Please guess a letter and press enter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in already_guessed:
            print('Letter has already been guessed, try again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please guess a LETTER from the English Alphabet.')
        else:
            return guess

def play_again():
    print('Do you want to play again? Yes or No?')
    return input().lower().startswith('y')

# Introduce the Game
print('Welcome to the Game by Noah.')
missed_letters = ''
correct_letters = ''
secret_word = get_randomword(words)
game_isdone = False

# Main Game Loop
while True:
    display_board(missed_letters, correct_letters, secret_word)

    guess = get_guess(missed_letters + correct_letters)

    if guess in secret_word:
        correct_letters = correct_letters + guess

        # Check To See If Winner, Winner Chicken Dinner
        found_allletters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_allletters = False
                break
            if found_allletters : # if True
                print('Imagine Winning, Could not be Me.')
                print('The secret word was' + secret_word)
                game_isdone = True

    if game_isdone:
        if play_again():
            missed_letters = ''
            correct_letters = ''

# i = 0
# while i < 50:
#     word = get_randomword(words)
#     print(word)
#     i += 1
