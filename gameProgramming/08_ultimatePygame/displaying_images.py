# Displaying Images, Noah Mulder, v1

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400)) # Display Surface: The window that the player sees when he starts the game. The Game Window. Anyhting displayed goes on here. Must be unique and is always visible
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

test_surface = pygame.Surface((100,200)) #(regular) surface: Essentially a single image (something imported, rendered text or a plain color). Needs to be put on display surface to be visible. Flexible amount and only displayed when connected to the display surface.
test_surface.fill('Red')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # draw all our elements
    # update everything
    screen.blit(test_surface, (0, 0)) # Origin, (0, 0), is in the top left corner of the display surface
    pygame.display.update()
    clock.tick(60)



