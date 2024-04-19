import pygame, random

# Initalize Pygame
pygame.init()
clock = pygame.time.Clock()

# Constants
resolution = 1 # 0 = Low Resolution (800, 600), 1 is High Resolution (1920, 1080)

int(input("What resolution would you like?\n 0 for Low\n 1 for High\n"))
if resolution == 0:
    x = 800
    y = 600
else:
    x = 1920
    y = 1080
screen = pygame.display.set_mode((x, y))
WIDTH = 800
HEIGHT = 600
CARD_WIDTH = 70
CARD_HEIGHT = 100
starting_screen = pygame.image.load('img/poker/yahoo.png').convert()
casino_setting = pygame.image.load('img/poker/casino_table.png').convert()
GREEN = (0, 128, 0)

difficulty = int(input("Please choose a difficulty. Enter 1 for EASY or 2 for HARD\n"))

if difficulty == 1:
    pygame.display.set_caption('G.Y.L.A -- EASY')
else:
    pygame.display.set_caption('G.Y.L.A -- CRACKED')

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Load card images
card_images = {}
for suit in ['hearts', 'diamonds', 'clubs', 'spades']:
    for rank in range(1, 14):
        card_images[(suit, rank)] = pygame.image.load(f'img/poker/PNG/Cards (large)/card_{suit}_{rank}.png')

# game loop
game_active = True
while game_active:
    if game_active:
        screen.blit(casino_setting, (0,0))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw player's hand
    player_hand = [(random.choice(['hearts', 'diamonds', 'clubs', 'spades']), random.randint(1, 13)) for _ in range(2)]
    for i, card in enumerate(player_hand):
        card_image = card_images[card]
        screen.blit(card_image, (300 + i * (CARD_WIDTH + 10), HEIGHT - 150))

    # Draw oppenent hand
    oppenent_hand = [(random.choice(['hearts', 'diamonds', 'clubs', 'spades']), random.randint(1, 13)) for _ in range(2)]
    for i, card in enumerate(oppenent_hand):
        card_image = pygame.image.load('img/poker/PNG/Cards (large)/card_back.png')
        screen.blit(card_image, (300 + i * (CARD_WIDTH + 10), 50))

    # Update the display
    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()