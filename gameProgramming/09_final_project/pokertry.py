import pygame, random

# Initalize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
CARD_WIDTH = 70
CARD_HEIGHT = 100
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Poker Game")

# Load card images
card_images = {}
for suit in ['hearts', 'diamonds', 'clubs', 'spades']:
    for rank in range(1, 14):
        card_images[(suit, rank)] = pygame.image.load(f'poker/PNG/Cards (large)/card_back.png')

# game loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw player's hand
    player_hand = [(random.choice(['hearts', 'diamonds', 'clubs', 'spades']), random.randint(1, 13)) for _ in range(5)]
    for i, card in enumerate(player_hand):
        card_image = card_images[card]
        screen.blit(card_image, (50 + i * (CARD_WIDTH + 10), HEIGHT - 150))