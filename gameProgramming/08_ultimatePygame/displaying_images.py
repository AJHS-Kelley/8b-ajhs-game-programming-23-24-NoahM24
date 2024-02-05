# Displaying Images, Noah Mulder, v1

#(regular) surface: Essentially a single image (something imported, rendered text or a plain color). Needs to be put on display surface to be visible. Flexible amount and only displayed when connected to the display surface.
# Display Surface: The window that the player sees when he starts the game. The Game Window. Anyhting displayed goes on here. Must be unique and is always visible
# Origin, (0, 0), is in the top left corner of the display surface
# Rectangles: Precise positioning of surfaces, basic collisions

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Weird Snail")
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

sky_surface = pygame.image.load('img/ultimate_pygame/sky.jpg').convert()
ground_surface = pygame.image.load('img/ultimate_pygame/ground.jpg').convert()

score_surf = test_font.render('Some Snail', False, 'Red')
score_rect = score_surf.get_rect(center = (400, 50))

snail_surface = pygame.image.load('img/ultimate_pygame/snailenemy.png').convert()
snail_rect = snail_surface.get_rect(topleft = (600, 170))

player_surf = pygame.image.load('img/ultimate_pygame/dude.png').convert()
player_rect = player_surf.get_rect(topleft = (80, 210))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # if event.type == pygame.MOUSEMOTION:
    #     if player_rect.collidepoint(event.pos): print('collision')
# draw all our elements
# update everything
    
    screen.blit(sky_surface, (0, 0))
    
    snail_rect.left -= 4
    if snail_rect.right <= 0: snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)
    
    screen.blit(player_surf, player_rect)
    
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, 'White', score_rect)
    pygame.draw.rect(screen, 'White', score_rect, 10)
    screen.blit(score_surf, score_rect)

    # if player_rect.colliderect(snail_rect):
    #    print('collision')
    
    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)



