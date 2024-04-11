# Final Project, Noah Mulder, v0
import sys, random, pygame

resolution = 1 # 0 = Low Resolution (800, 600), 1 is High Resolution (1920, 1080)

int(input("What resolution would you like?\n 0 for Low\n 1 for High\n"))
if resolution == 0:
    x = 800
    y = 600
else:
    x = 1920
    y = 1080
screen = pygame.display.set_mode((x, y))

pygame.init()
clock = pygame.time.Clock()
game_active = True

starting_screen = pygame.image.load('img/poker/yahoo.png').convert()

difficulty = int(input("Please choose a difficulty. Enter 1 for EASY or 2 for HARD\n"))

if difficulty == 1:
    pygame.display.set_caption('G.Y.L.A -- EASY')
else:
    pygame.display.set_caption('G.Y.L.A -- CRACKED')

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
    
    if game_active:
        screen.blit(starting_screen, (0,0))