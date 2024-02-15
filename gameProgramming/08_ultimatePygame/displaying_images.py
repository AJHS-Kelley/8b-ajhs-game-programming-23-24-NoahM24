# Displaying Images, Noah Mulder, v1

#(regular) surface: Essentially a single image (something imported, rendered text or a plain color). Needs to be put on display surface to be visible. Flexible amount and only displayed when connected to the display surface.
# Display Surface: The window that the player sees when he starts the game. The Game Window. Anyhting displayed goes on here. Must be unique and is always visible
# Origin, (0, 0), is in the top left corner of the display surface
# Rectangles: Precise positioning of surfaces, basic collisions

import pygame
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Death Trap for the User")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = True
start_time = 0

sky_surface = pygame.image.load('img/ultimate_pygame/Sky.png').convert()
ground_surface = pygame.image.load('img/ultimate_pygame/ground.png').convert()

# score_surf = test_font.render('Some Snail', False, 'Red')
# score_rect = score_surf.get_rect(center = (400, 50))

snail_surface = pygame.image.load('img/ultimate_pygame/snail1.png').convert()
snail_rect = snail_surface.get_rect(bottomright = (600, 300))


player_surf = pygame.image.load('img/ultimate_pygame/player_walk_1.png').convert()
player_rect = player_surf.get_rect(topleft = (80, 210))
player_gravity = 0
player_stand = pygame.image.load('img/ultimate_pygame/homer_nipp.png').convert()
player_stand_scaled = pygame.transform.scale(player_stand, (600, 300))
player_stand_rect = player_stand.get_rect(center = (400, 200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if game_active:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300: 
                player_gravity = -20

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                player_gravity = -20
    else:
        if event.type == pygame.MOUSEBUTTONDOWN:
            game_active = True
            snail_rect.left = 800
            start_time = int(pygame.time.get_ticks() / 1000)

# draw all our elements
# update everything
    if game_active:
        #SKY    
        screen.blit(sky_surface, (0, 0))
        #SNAIL
        snail_rect.left -= 6
        if snail_rect.right <= 0: snail_rect.left = 800
        screen.blit(snail_surface, snail_rect)
        
        #PLAYER
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        #GROUND
        screen.blit(ground_surface, (0, 300))
        # pygame.draw.rect(screen, 'White', score_rect)
        # pygame.draw.rect(screen, 'White', score_rect, 10)
        # screen.blit(score_surf, score_rect)
        display_score()

        #COLLISION
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand_scaled, player_stand_rect)

    pygame.display.update()
    clock.tick(60)



