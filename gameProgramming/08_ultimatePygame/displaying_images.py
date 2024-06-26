# Displaying Images, Noah Mulder, v1

# Almost done, please complete! 

# (regular) surface: Essentially a single image (something imported, rendered text or a plain color). Needs to be put on display surface to be visible. Flexible amount and only displayed when connected to the display surface.
# Display Surface: The window that the player sees when he starts the game. The Game Window. Anyhting displayed goes on here. Must be unique and is always visible
# Origin, (0, 0), is in the top left corner of the display surface
# Rectangles: Precise positioning of surfaces, basic collisions

import pygame
from sys import exit
from random import randint

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300: screen.blit(snail_surface, obstacle_rect)
            else: screen.blit(fly_surf, obstacle_rect)
            
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else: return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True

def player_animation():
    global player_surf, player_index

    if player_rect.bottom < 300:
        player_surf = player_jump
        # jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk): player_index = 0
        player_surf = player_walk[int(player_index)]
        # walk
    # play walking animation if the player is on the floor
    # display jumping animation when player is not on the floor

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Death Trap for the User")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = True
start_time = 0
score = 0

sky_surface = pygame.image.load('img/ultimate_pygame/Sky.png').convert()
ground_surface = pygame.image.load('img/ultimate_pygame/ground.png').convert()

# score_surf = test_font.render('Some Snail', False, 'Red')
# score_rect = score_surf.get_rect(center = (400, 50))

# Obstacles
snail_surface = pygame.image.load('img/ultimate_pygame/snail1.png').convert()
snail_surf2 = pygame.image.load('img/ultimate_pygame/snail2.png').convert()
snail_frames = [snail_surface, snail_surf2]
snail_frame_index = 0
snail_surf = snail_frames[snail_frame_index]

fly_surf = pygame.image.load('img/ultimate_pygame/Fly1.png').convert()
fly_surf2 = pygame.image.load('img/ultimate_pygame/Fly2.png').convert()
fly_frames = [fly_surf, fly_surf2]
fly_frame_index = 0
fly_surface = fly_frames[fly_frame_index]

obstacle_rect_list = []


player_walk_1 = pygame.image.load('img/ultimate_pygame/mario.png').convert()
player_walk_2 = pygame.image.load('img/ultimate_pygame/mario2.png').convert()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load('img/ultimate_pygame/sanicjump.png').convert()

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(topleft = (80, 210))
player_gravity = 0


player_stand = pygame.image.load('img/ultimate_pygame/homer_nipp.png').convert()
player_stand_scaled = pygame.transform.scale(player_stand, (600, 300))
player_stand_rect = player_stand.get_rect(center = (400, 190))

game_name = test_font.render('Death Trap for the User', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center = (400, 40))

game_message = test_font.render('Click screen to run', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center = (400, 380))


# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1400)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if game_active:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300: 
                player_gravity = -50000

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                player_gravity = -20
    else:
        if event.type == pygame.MOUSEBUTTONDOWN:
            game_active = True
            start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        if event.type == obstacle_timer:
            if randint(0, 2):
                obstacle_rect_list.append(snail_surface.get_rect(bottomright = (randint(900, 1100), 300)))
            else:
                obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900, 1100), 210)))
        
        if event.type == snail_animation_timer:
            if snail_frame_index == 0: snail_frame_index = 1
    



# draw all our elements
# update everything
    if game_active:
        # SKY    
        screen.blit(sky_surface, (0, 0))
        # SNAIL
        # snail_rect.left -= 10
        # if snail_rect.right <= 0: snail_rect.left = 800
        # screen.blit(snail_surface, snail_rect)
        
        # PLAYER
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        player_animation()
        screen.blit(player_surf, player_rect)

        # OBSTACLE MOVEMENT
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        #collisions
        game_active = collisions(player_rect, obstacle_rect_list)

        # GROUND
        screen.blit(ground_surface, (0, 300))
        # pygame.draw.rect(screen, 'White', score_rect)
        # pygame.draw.rect(screen, 'White', score_rect, 10)
        # screen.blit(score_surf, score_rect)
        score = display_score()

    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand_scaled, player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_gravity = 0

        score_message = test_font.render(f'Your Score: {score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center = (400, 380))
        screen.blit(game_name, game_name_rect)

        if score == 0: screen.blit(game_message, game_message_rect)
        else: screen.blit(score_message, score_message_rect)


    pygame.display.update()
    clock.tick(60)



