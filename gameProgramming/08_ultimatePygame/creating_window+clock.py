# Creating Window and Clock, Noah Mulder, v1

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400)) # Display Surface: The window that the player sees when he starts the game
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # draw all our elements
    # update everything
    pygame.display.update()
    clock.tick(60)