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
test_font = pygame.font.Font(None, 50)

sky_surface = pygame.image.load('img/ultimate_pygame/sky.jpg').convert()
ground_surface = pygame.image.load('img/ultimate_pygame/ground.jpg').convert()
text_surface = test_font.render('My Game', False, 'Green')

snail_surface = pygame.image.load('img/ultimate_pygame/snailenemy.png').convert()
snail_x_pos = 600

player_surf = pygame.image.load('img/ultimate_pygame/dude.png').convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # draw all our elements
    # update everything
    
    screen.blit(sky_surface, (0, 0))
    snail_x_pos -= 4
    if snail_x_pos < -170: snail_x_pos = 800
    screen.blit(snail_surface, (snail_x_pos, 170))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))

    pygame.display.update()
    clock.tick(60)



