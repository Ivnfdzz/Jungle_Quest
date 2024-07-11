import pygame
from settings import *
from tools import *
from loads import *

pygame.init()
pygame.mixer.init()

# Screen config
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
# Window title
pygame.display.set_caption('Jungle Quest')
pygame.display.set_icon(pygame.image.load("./src/assets/images/gui/icon.png"))
clock = pygame.time.Clock()
# Font settings
font = pygame.font.SysFont("Daydream", 30)

def level_1():
    #level1
    while True:
        pygame.mixer_music.play()
        # Player
        player = create_player()
        
        # Enemy "trunk"
        trunk = create_trunk(1, "left")
        
        # Enemy "rino"
        rino = create_rino(1, "left")
        
        # Map
        platforms = create_level_platforms(1)
        
        # Game
        game = game_flags()
        # Game loop
        while True:
            clock.tick(FPS)
            # Event detection
            if not game["game_over"]:
                if game["show_popup"]:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            quit_game()
                        if event.type == KEYDOWN and event.key == K_SPACE:
                            game["show_popup"] = False
                    SCREEN.blit(start_popup, (0, 0))
                    pygame.display.flip()
                    continue 
            
            if game["game_over"]:
                game["show_popup"] = True
                for event in pygame.event.get():
                    if event.type == QUIT:
                        quit_game()
                    if event.type == KEYDOWN and event.key == K_SPACE:
                        game["show_popup"] = False
                        level_1()
                SCREEN.blit(fail_gameover_popup, (0, 0))
                pygame.display.flip()
                continue

            for event in pygame.event.get():
                if event.type == QUIT:
                    quit_game()
                
                # Press keys detection
                keydown_detection(event, player, game, SCREEN, font)
                    
                # Release keys detection
                keyup_detection(event, player)

            # Player
            launch_player_events(player, platforms, SCREEN)
            
            game["game_over"] = check_player_death(player, game)
            
            SCREEN.blit(level_1_background, (0, 0))
            #Rino enemy:
            launch_rino_events(rino, player, SCREEN, 1)
            
            # Trunk enemy
            launch_trunk_events(trunk, player, SCREEN)
            
            # Player animation
            show_animation(SCREEN, player["animation"], 10, player["hitbox"]["rct"].x, player["hitbox"]["rct"].y)
            
            # Drawings
            launch_drawing_events(player, SCREEN, trunk, game, font)
            
            # Hearts hud updating
            get_health_image(player)
            
            playtime = pygame.time.get_ticks()
            
            if level_1_condition(trunk, rino, player):
                level_2(player, playtime)
            
            SCREEN.blit(player["heart_image"], (HEARTS_GUI_POSITION[0], HEARTS_GUI_POSITION[1]))
            SCREEN.blit(stars_hud, (STARS_POSITION[0], STARS_POSITION[1]))
            show_text(SCREEN, (STARS_POSITION[0] + 80, STARS_POSITION[1] + 25), f"{player["stars_count"]}", font, YELLOW)
            
            # Refresh screen
            pygame.display.flip()

def level_2(past_player, playtime):
    #level 2
    while True:
        pygame.mixer_music.play()
        # Player
        
        player = create_player(player_hearts= past_player["hearts"], heart_image= past_player["heart_image"],got_invulnerability_star= False, stars_count= past_player["stars_count"])
        
        # Enemy "trunk"
        
        trunk = create_trunk(2, "left")
        
        # Enemy "trunk 2"
        trunk_2 = create_trunk(3, "right")
        
        # Enemy "rino"
        rino = create_rino(2, "left")
        
        # Map
        platforms = create_level_platforms(2)
        
        # Game
        game = game_flags()
        game["playtime"] = playtime

        while True:
            clock.tick(FPS)
            
            if game["game_over"]:
                game["show_popup"] = True
                for event in pygame.event.get():
                    if event.type == QUIT:
                        quit_game()
                    if event.type == KEYDOWN and event.key == K_SPACE:
                        game["show_popup"] = False
                        level_1()
                SCREEN.blit(fail_gameover_popup, (0, 0))
                pygame.display.flip()
                continue
            
            # Event detection
            for event in pygame.event.get():
                if event.type == QUIT:
                    quit_game()
                
                keydown_detection(event, player, game, SCREEN, font)
                # Release keys detection
                keyup_detection(event, player)

            launch_player_events(player, platforms, SCREEN)
            
            game["game_over"] = check_player_death(player, game)
            
            SCREEN.blit(level_2_background, (0, 0))
            
            #Rino enemy:
            launch_rino_events(rino, player, SCREEN, 2)
            
            # Trunk enemy
            launch_trunk_events(trunk, player, SCREEN)
            
            # trunk_2 enemy
            launch_trunk_events(trunk_2, player, SCREEN)
            
            # Player animation
            show_animation(SCREEN, player["animation"], 10, player["hitbox"]["rct"].x, player["hitbox"]["rct"].y)
            
            # Drawings
            launch_drawing_events(player, SCREEN, [trunk, trunk_2], game, font)
            
            get_health_image(player)
            
            display_and_check_invulnerability_star(player, SCREEN, game)

            show_star_popup(game, SCREEN)
            
            new_playtime = playtime + pygame.time.get_ticks()
            if level_2_condition(trunk, rino, trunk_2, player):
                level_3(player, new_playtime)

            SCREEN.blit(player["heart_image"], (HEARTS_GUI_POSITION[0], HEARTS_GUI_POSITION[1]))
            SCREEN.blit(stars_hud, (STARS_POSITION[0], STARS_POSITION[1]))
            show_text(SCREEN, (STARS_POSITION[0] + 80, STARS_POSITION[1] + 25), f"{player["stars_count"]}", font, YELLOW)
            # Refresh screen
            pygame.display.flip()

def level_3(past_player, playtime):
    while True:
        pygame.mixer_music.play()
        # Player
        player = create_player(player_hearts= past_player["hearts"], heart_image= past_player["heart_image"],got_invulnerability_star= past_player["got_invulnerability_star"], stars_count= past_player["stars_count"])
        
        # Enemy "trunk"
        trunk = create_trunk(4, "left")
        
        # Enemy "trunk 2"
        trunk_2 = create_trunk(5, "right")
        
        # Enemy "rino"
        rino = create_rino_block(3, "left")
        
        # Enemy "rino 2"
        rino_2 = create_rino_block(4, "left")
        
        # Enemy "rino_3"
        rino_3 = create_rino_block(5, "right")
        
        # Map
        platforms = create_level_platforms(3)
        
        # Game
        game = game_flags()
        game["playtime"] = new_playtime
        # Game loop
        while True:
            clock.tick(FPS)
            
            if game["game_over"]:
                game["show_popup"] = True
                for event in pygame.event.get():
                    if event.type == QUIT:
                        quit_game()
                    if event.type == KEYDOWN and event.key == K_SPACE:
                        game["show_popup"] = False
                        level_1()
                SCREEN.blit(fail_gameover_popup, (0, 0))
                pygame.display.flip()
                continue
            
            # Event detection
            for event in pygame.event.get():
                if event.type == QUIT:
                    quit_game()
                
                keydown_detection(event, player, game, SCREEN, font)
                # Release keys detection
                keyup_detection(event, player)

            launch_player_events(player, platforms)
            
            game["game_over"] = check_player_death(player, game)
            
            # Showing images and animations
            SCREEN.blit(level_3_background, (0, 0))
            
            # Trunk enemy
            launch_trunk_events(trunk, player, SCREEN)
            
            # Trunk 2 enemy
            launch_trunk_events(trunk_2, player, SCREEN)
            
            #Rino enemy:
            launch_rino_events(rino, player, SCREEN, 3)
            
            #Rino enemy:
            launch_rino_events(rino_2, player, SCREEN, 4)
            
            #Rino enemy:
            launch_rino_events(rino_3, player, SCREEN, 5)
            
            # Player animation
            show_animation(SCREEN, player["animation"], 10, player["hitbox"]["rct"].x, player["hitbox"]["rct"].y)
            
            # Draw the player laser
            launch_drawing_events(player, SCREEN, [trunk, trunk_2], game, font)
            
            get_health_image(player)
            
            
            new_playtime = playtime + pygame.time.get_ticks()
            if level_3_condition(trunk, rino, trunk_2, rino_2, rino_3, player):
                level_4(player, new_playtime)
            
            SCREEN.blit(player["heart_image"], (HEARTS_GUI_POSITION[0], HEARTS_GUI_POSITION[1]))
            SCREEN.blit(stars_hud, (STARS_POSITION[0], STARS_POSITION[1]))
            show_text(SCREEN, (STARS_POSITION[0] + 80, STARS_POSITION[1] + 25), f"{player["stars_count"]}", font, YELLOW)
            
            # Refresh screen
            pygame.display.flip()

def level_4(player_hearts, heart_image, stars_count, got_invulnerability_star, playtime):
    #level4
    while True:
        pygame.mixer_music.play()
        # Player
        player = create_player_block()
        player_hearts = player_hearts
        heart_image = heart_image
        move_left = False
        move_right = False
        player_direction = "right"
        double_jump_used = False
        player_laser = None
        player_laser_direction = None
        player_hit_invulnerability = False
        player_hit_invulnerability_start_time = 0
        got_artifact = False
        got_invulnerability_star = got_invulnerability_star
        inv_star_on = False
        star_invulnerability_start_time = 0
        inv_star_used = False
        shooting = False
        stars_count = stars_count
        artifact_rect = pygame.Rect(ARTIFACT_POSITION[0], ARTIFACT_POSITION[1], ARTIFACT_SIZE[0], ARTIFACT_SIZE[1])
        
        # Enemy "rino"
        rino = create_rino_block(6)
        rino_live = True
        rino_direction = "left"
        rino_animation = None
        
        # Enemy "rino 2"
        rino_2 = create_rino_block(7)
        rino_2_live = True
        rino_2_direction = "left"
        rino_2_animation = None
        
        # Enemy "rino_3"
        rino_3 = create_rino_block(8)
        rino_3_live = True
        rino_3_direction = "right"
        rino_3_animation = None
        
        # Enemy "rino_4"
        rino_4 = create_rino_block(9)
        rino_4_live = True
        rino_4_direction = "right"
        rino_4_animation = None
        
        # Enemy "trunk"
        trunk = create_trunk(6)
        trunk_animation = None
        trunk_bullet = None
        trunk_live = True
        trunk_vision = create_platform(0, 100, 800, 80, color=RED)
        
        # Enemy "trunk 2"
        trunk_2 = create_trunk(7)
        trunk_2_animation = None
        trunk_2_bullet = None
        trunk_2_live = True
        trunk_2_vision = create_platform(0, 100, 800, 80, color=RED)
        
        # Visual effects
        visual_effect = None
        visual_effect_animation = None
        visual_effect_location = None
        
        # Map
        platforms = [
            create_platform(0, SCREEN_HEIGHT - 80, SCREEN_WIDTH, 80, color=GREEN),
            create_platform(0, 220, 800, 1, color=RED),
            create_platform(0, 370, 800, 1, color=RED),
        ]
        
        # Game
        playing_music = True
        in_pause = False
        show_popup = False
        playtime = playtime
        new_playtime = 0
        game_over = False
        continue_game = False
        # Game loop
        while True:
            clock.tick(FPS)
            
            if game_over:
                show_popup = True
                for event in pygame.event.get():
                    if event.type == QUIT:
                        quit_game()
                    if event.type == KEYDOWN and event.key == K_SPACE:
                        show_popup = False
                        level_1()
                SCREEN.blit(fail_gameover_popup, (0, 0))
                pygame.display.flip()
                continue
            
            # Event detection
            for event in pygame.event.get():
                if event.type == QUIT:
                    quit_game()
                
                # Press keys detection
                if event.type == KEYDOWN:
                    # Movement keys
                    if event.key == K_SPACE or event.key == K_UP:
                        if player["on_ground"]:
                            player["vel_y"] = -JUMP_STRENGTH
                            player["on_ground"] = False
                        elif not player["double_jump_used"]:
                            player["vel_y"] = -JUMP_2_STRENGTH
                            player["double_jump_used"] = True
                    
                    if event.key == K_LEFT or event.key == K_a:
                        move_left = True
                        last_player_direction = "left"
                        player_direction = "left"
                    
                    if event.key == K_RIGHT or event.key == K_d:
                        move_right = True
                        last_player_direction = "right"
                        player_direction = "right"
                        
                    if event.key == K_DOWN or event.key == K_s:
                        move_down = True
                    
                    # Mute
                    if event.key == K_m:
                        if playing_music:
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()
                        playing_music = not playing_music
                    
                    # Pause
                    if event.key == K_p:
                        pass
                    
                    # Shoot
                    if event.key == K_LSHIFT:
                        if not player_laser:
                            shooting = True
                            shooting_timer = pygame.time.get_ticks()
                            player_laser = create_laser(player["rct"].midright if player_direction == "right" else player["rct"].midleft)
                            player_laser_direction = player_direction
                    
                    if event.key == K_x:
                        if got_invulnerability_star:
                            if not inv_star_used:
                                inv_star_on = True
                                star_invulnerability_start_time = pygame.time.get_ticks()
                                inv_star_used = True
                # Release keys detection
                if event.type == KEYUP:
                    if event.key == K_LEFT or event.key == K_a:
                        move_left = False
                    if event.key == K_DOWN or event.key == K_s:
                        move_down = False
                    if event.key == K_RIGHT or event.key == K_d:
                        move_right = False

            # Applying constant gravity
            player["vel_y"] += GRAVITY
            player["rct"].y += player["vel_y"]
            
            # Check collision with ground
            if player["rct"].bottom >= GROUND_LEVEL:
                player["rct"].bottom = GROUND_LEVEL
                player["vel_y"] = 0
                player["on_ground"] = True
                player["double_jump_used"] = False
                player_animation = get_animation_direction(player_idle_right, player_idle_left, player_direction)
            
            player = check_player_enviorment_collitions(player, platforms)
            
            # Player movement
            if move_left and not move_right and player["rct"].left > 0:
                player["rct"].x -= PJ_SPEED
                player_direction = "left"
            if move_right and not move_left and player["rct"].right < SCREEN_WIDTH:
                player["rct"].x += PJ_SPEED
                player_direction = "right"
            
            # Update player animation
            if not player["on_ground"]:
                player_animation = get_animation_direction(player_jump_right, player_jump_left, player_direction)
            elif shooting:
                if move_left or move_right:
                    player_animation = get_animation_direction(player_running_shoot_right, player_running_shoot_left, player_direction)
                else:
                    player_animation = get_animation_direction(player_shoot_right, player_shoot_left, player_direction)
                
                if pygame.time.get_ticks() - shooting_timer > 200:  
                    shooting = False

            elif move_left or move_right:
                player_animation = get_animation_direction(player_run_right, player_run_left, player_direction)
            else:
                player_animation = get_animation_direction(player_idle_right, player_idle_left, player_direction)
            
            # Update player laser position and check if it goes out of screen
            if player_laser:
                if player_laser_direction == "right":
                    player_laser["rct"].x += player_laser["speed"]
                else:
                    player_laser["rct"].x -= player_laser["speed"]
                
                if player_laser["rct"].right < 0 or player_laser["rct"].left > SCREEN_WIDTH:
                    player_laser = None
            
            if player_hit_invulnerability == True:
                current_time = pygame.time.get_ticks()
                if current_time - player_hit_invulnerability_start_time > PLAYER_HIT_INVULNERABILITY_DURATION:
                    player_hit_invulnerability = False
            # Showing images and animations
            SCREEN.blit(level_4_background, (0, 0))
            
            if inv_star_on:
                current_time = pygame.time.get_ticks()
                if current_time - star_invulnerability_start_time < INVULNERABILITY_STAR_DURATION:
                    shield_x = player["rct"].centerx - inv_star_shield.get_width() // 2
                    shield_y = player["rct"].centery - inv_star_shield.get_height() // 2
                    SCREEN.blit(inv_star_shield, (shield_x, shield_y))
                else:
                    inv_star_on = False
                    star_invulnerability_start_time = None
            
            if player_hearts <= 0:
                game_over = True
                
            #Rino enemy:
            if rino_live:
                if rino_direction == "left":
                    rino["rct"].x -= RINO_SPEED
                    rino_animation = rino_run_right
                    if rino["rct"].left <= 0:
                        rino_direction = "right"
                else:
                    rino["rct"].x += RINO_SPEED
                    rino_animation = rino_run_left
                    if rino["rct"].right >= SCREEN_WIDTH:
                        rino_direction = "left"
                
                if not inv_star_on:
                    if player_hit_invulnerability == False:
                        if detectar_colision(player["rct"], rino["rct"]):
                            player_hearts -= 1
                            if rino_direction == "left":
                                player["rct"].x += 20
                            else:
                                player["rct"].x -= 20
                            player["vel_y"] = -JUMP_STRENGTH + 5 
                            player_hit_invulnerability = True
                            player_hit_invulnerability_start_time = pygame.time.get_ticks()
                
                if player_laser:
                    if detectar_colision(player_laser["rct"], rino["rct"]):
                        rino_live = None
                        player_laser = None
                        stars_count += 1
                        visual_effect = True
                        visual_effect_start_time = pygame.time.get_ticks()
                        visual_effect_animation = item_feedback
                        visual_effect_location = rino["rct"][0], rino["rct"][1]
                show_animation(SCREEN, rino_animation, 10, rino["rct"].x, rino["rct"].y)
            
            #Rino enemy:
            if rino_2_live:
                if rino_2_direction == "left":
                    rino_2["rct"].x -= RINO_SPEED
                    rino_2_animation = rino_run_right
                    if rino_2["rct"].left <= 0:
                        rino_2_direction = "right"
                else:
                    rino_2["rct"].x += RINO_SPEED
                    rino_2_animation = rino_run_left
                    if rino_2["rct"].right >= SCREEN_WIDTH:
                        rino_2_direction = "left"
                
                if not inv_star_on:
                    if player_hit_invulnerability == False:
                        if detectar_colision(player["rct"], rino_2["rct"]):
                            player_hearts -= 1
                            if rino_2_direction == "left":
                                player["rct"].x += 20
                            else:
                                player["rct"].x -= 20
                            player["vel_y"] = -JUMP_STRENGTH + 5 
                            player_hit_invulnerability = True
                            player_hit_invulnerability_start_time = pygame.time.get_ticks()
                
                if player_laser:
                    if detectar_colision(player_laser["rct"], rino_2["rct"]):
                        rino_2_live = None
                        player_laser = None
                        stars_count += 1
                        visual_effect = True
                        visual_effect_start_time = pygame.time.get_ticks()
                        visual_effect_animation = item_feedback
                        visual_effect_location = rino_2["rct"][0], rino_2["rct"][1]
                show_animation(SCREEN, rino_2_animation, 10, rino_2["rct"].x, rino_2["rct"].y)
            
            if rino_3_live:
                if rino_3_direction == "left":
                    rino_3["rct"].x -= RINO_SPEED
                    rino_3_animation = rino_run_right
                    if rino_3["rct"].left <= 0:
                        rino_3_direction = "right"
                else:
                    rino_3["rct"].x += RINO_SPEED
                    rino_3_animation = rino_run_left
                    if rino_3["rct"].right >= SCREEN_WIDTH:
                        rino_3_direction = "left"
                
                if not inv_star_on:
                    if player_hit_invulnerability == False:
                        if detectar_colision(player["rct"], rino_3["rct"]):
                            player_hearts -= 1
                            if rino_3_direction == "left":
                                player["rct"].x += 20
                            else:
                                player["rct"].x -= 20
                            player["vel_y"] = -JUMP_STRENGTH + 5 
                            player_hit_invulnerability = True
                            player_hit_invulnerability_start_time = pygame.time.get_ticks()
                
                if player_laser:
                    if detectar_colision(player_laser["rct"], rino_3["rct"]):
                        rino_3_live = None
                        player_laser = None
                        stars_count += 1
                        visual_effect = True
                        visual_effect_start_time = pygame.time.get_ticks()
                        visual_effect_animation = item_feedback
                        visual_effect_location = rino_3["rct"][0], rino_3["rct"][1]
                show_animation(SCREEN, rino_3_animation, 10, rino_3["rct"].x, rino_3["rct"].y)
            
            if rino_4_live:
                if rino_4_direction == "left":
                    rino_4["rct"].x -= RINO_SPEED
                    rino_4_animation = rino_run_right
                    if rino_4["rct"].left <= 0:
                        rino_4_direction = "right"
                else:
                    rino_4["rct"].x += RINO_SPEED
                    rino_4_animation = rino_run_left
                    if rino_4["rct"].right >= SCREEN_WIDTH:
                        rino_4_direction = "left"
                
                if not inv_star_on:
                    if player_hit_invulnerability == False:
                        if detectar_colision(player["rct"], rino_4["rct"]):
                            player_hearts -= 1
                            if rino_4_direction == "left":
                                player["rct"].x += 20
                            else:
                                player["rct"].x -= 20
                            player["vel_y"] = -JUMP_STRENGTH + 5 
                            player_hit_invulnerability = True
                            player_hit_invulnerability_start_time = pygame.time.get_ticks()
                
                if player_laser:
                    if detectar_colision(player_laser["rct"], rino_4["rct"]):
                        rino_4_live = None
                        player_laser = None
                        stars_count += 1
                        visual_effect = True
                        visual_effect_start_time = pygame.time.get_ticks()
                        visual_effect_animation = item_feedback
                        visual_effect_location = rino_4["rct"][0], rino_4["rct"][1]
                show_animation(SCREEN, rino_4_animation, 10, rino_4["rct"].x, rino_4["rct"].y)
            
            if trunk_live:
                # Trunk's defeat
                if player_laser:
                    if detectar_colision(player_laser["rct"], trunk["rct"]):
                        trunk_live = False
                        player_laser = None
                        stars_count += 1
                        visual_effect = True
                        visual_effect_start_time = pygame.time.get_ticks()
                        visual_effect_animation = item_feedback
                        visual_effect_location = trunk["rct"][0], trunk["rct"][1]
                # Making trunk able to shoot
                if detectar_colision(player["rct"], trunk_vision["rect"]):
                    trunk_animation = trunk_attack_right
                    # Setting a time between each trunk's shoot and creating the shoot
                    if pygame.time.get_ticks() - trunk["last_shoot_time"] > TRUNK_SHOOT_TIME:
                        trunk["last_shoot_time"] = pygame.time.get_ticks()
                        trunk_bullet = create_laser(trunk["rct"].midleft, color=YELLOW)
                # Trunk shoot movement
                if trunk_bullet:
                    trunk_bullet["rct"].x -= trunk_bullet["speed"]
                # Trunk shoot hit player
                    if not inv_star_on:
                        if player_hit_invulnerability == False:
                            if detectar_colision(player["rct"], trunk_bullet["rct"]):
                                player_hearts -= 1
                                trunk_bullet = None
                #If there is no interatction with player, trunk animation = idle
                else:
                    trunk_animation = trunk_idle_right
                show_animation(SCREEN, trunk_animation, 10, trunk["rct"].x, trunk["rct"].y)
            # Player animation
            show_animation(SCREEN, player_animation, 10, player["rct"].x, player["rct"].y)
            
            if trunk_2_live:
                # trunk_2's defeat
                if player_laser:
                    if detectar_colision(player_laser["rct"], trunk_2["rct"]):
                        trunk_2_live = False
                        player_laser = None
                        stars_count += 1
                        visual_effect = True
                        visual_effect_start_time = pygame.time.get_ticks()
                        visual_effect_animation = item_feedback
                        visual_effect_location = trunk_2["rct"][0], trunk_2["rct"][1]
                # Making trunk_2 able to shoot
                if detectar_colision(player["rct"], trunk_2_vision["rect"]):
                    trunk_2_animation = trunk_attack_left
                    # Setting a time between each trunk_2's shoot and creating the shoot
                    if pygame.time.get_ticks() - trunk_2["last_shoot_time"] > TRUNK_SHOOT_TIME:
                        trunk_2["last_shoot_time"] = pygame.time.get_ticks()
                        trunk_2_bullet = create_laser(trunk_2["rct"].midright, color=YELLOW)
                # trunk_2 shoot movement
                if trunk_2_bullet:
                    trunk_2_bullet["rct"].x += trunk_2_bullet["speed"]
                # trunk_2 shoot hit player
                    if not inv_star_on:
                        if player_hit_invulnerability == False:
                            if detectar_colision(player["rct"], trunk_2_bullet["rct"]):
                                player_hearts -= 1
                                trunk_2_bullet = None
                #If there is no interatction with player, trunk_2 animation = idle
                else:
                    trunk_2_animation = trunk_idle_left
                show_animation(SCREEN, trunk_2_animation, 10, trunk_2["rct"].x, trunk_2["rct"].y)
            
            # Draw the player laser
            if player_laser:
                pygame.draw.rect(SCREEN, player_laser["color"], player_laser["rct"])

            if trunk_bullet:
                if not trunk_live:
                    trunk_bullet = None
                else:
                    pygame.draw.rect(SCREEN, trunk_bullet["color"], trunk_bullet["rct"])
            
            if trunk_2_bullet:
                if not trunk_2_live:
                    trunk_2_bullet = None
                else:
                    pygame.draw.rect(SCREEN, trunk_2_bullet["color"], trunk_2_bullet["rct"])
            
            if visual_effect:
                if pygame.time.get_ticks() - visual_effect_start_time < VISUAL_EFFECT_DURATION:
                    show_animation(SCREEN, visual_effect_animation, 10, visual_effect_location[0], visual_effect_location[1])
                else:
                    visual_effect = False
            
            match player_hearts:
                case 5:
                    heart_image = hearts_5
                case 4:
                    heart_image = hearts_4
                case 3:
                    heart_image = hearts_3
                case 2:
                    heart_image = hearts_2
                case 1:
                    heart_image = hearts_1
                case 0:
                    heart_image = hearts_0
            
            
            if not trunk_live and not trunk_2_live and not rino_live and not rino_2_live and not rino_3_live:
                SCREEN.blit(artifact_image, (ARTIFACT_POSITION[0], ARTIFACT_POSITION[1]))
                if not got_artifact:
                    if detectar_colision(player["rct"], artifact_rect):
                        got_artifact = True
                        show_popup = True
                        popup_start_time = pygame.time.get_ticks()
            
            new_playtime = playtime + pygame.time.get_ticks()
            SCREEN.blit(heart_image, (HEARTS_GUI_POSITION[0], HEARTS_GUI_POSITION[1]))
            SCREEN.blit(stars_hud, (STARS_POSITION[0], STARS_POSITION[1]))
            show_text(SCREEN, (STARS_POSITION[0] + 80, STARS_POSITION[1] + 25), f"{stars_count}", font, YELLOW)
            
            if show_popup:
                current_time = pygame.time.get_ticks()
                if current_time - popup_start_time >= POPUP_DURATION:
                    show_popup = False
                    quit_game()
                    break  # Salir del bucle principal
                else:
                    SCREEN.blit(gameover_popup, (0,0))
            if got_artifact:
                show_popup = True
            # Refresh screen
            pygame.display.flip()