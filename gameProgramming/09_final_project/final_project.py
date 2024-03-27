# Final Project, Noah Mulder, v0
import pygame
from sys import exit
import random
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Death Trap for the User")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()