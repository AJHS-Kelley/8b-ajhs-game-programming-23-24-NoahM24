# Displaying Images, Noah Mulder, v1
#(regular) surface: Essentially a single image (something imported, rendered text or a plain color). Needs to be put on display surface to be visible. Flexible amount and only displayed when connected to the display surface.
# Display Surface: The window that the player sees when he starts the game. The Game Window. Anyhting displayed goes on here. Must be unique and is always visible
# Origin, (0, 0), is in the top left corner of the display surface

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

sky_surface = pygame.image.load('img/ultimate_pygame/sky.jfif')
ground_surface = pygame.image.load('img/ultimate_pygame/ground.jfif')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # draw all our elements
    # update everything
    screen.blit(ground_surface(0, 100))
    screen.blit(sky_surface, (0, 0))
    pygame.display.update()
    clock.tick(60)



