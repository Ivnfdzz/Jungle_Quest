import pygame
from settings import *
from tools import *
from loads import *

pygame.init()
pygame.mixer.init()

# Screen config
SCREEN = pygame.display.set_mode(SCREEN_SIZE)

clock = pygame.time.Clock()
# Font settings
font = pygame.font.SysFont("Daydream", 30)
pygame.mixer_music.play()

def level_1():
    #level1
    while True:
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
        game["show_popup"] = True
        
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
                keydown_detection(event, player, game, SCREEN, font, platforms)
                    
                # Release keys detection
                keyup_detection(event, player)
            
            # Player
            launch_player_events(player, platforms, SCREEN)
            game["game_over"] = check_player_death(player, game, SCREEN, font)
            
            SCREEN.blit(level_1_background, (0, 0))
            #Rino enemy:
            launch_rino_events(rino, player, SCREEN, 1)
            
            # Trunk enemy
            launch_trunk_events(trunk, player, SCREEN)
            
            # Player animation
            show_animation(SCREEN, player["animation"], 10, player["hitbox"]["rct"].x, player["hitbox"]["rct"].y)
            
            # Drawings
            launch_drawing_events(player, SCREEN, trunk, game, font)
            
            # GUI
            show_hud(SCREEN, player, font)
            
            player["score"] = score_calculator(player)
            if level_1_condition(trunk, rino, player):
                level_2(player)
            
            # Refresh screen
            pygame.display.flip()

def level_2(past_player):
    #level 2
    while True:
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
                
                keydown_detection(event, player, game, SCREEN, font, platforms)
                # Release keys detection
                keyup_detection(event, player)

            launch_player_events(player, platforms, SCREEN)
            
            game["game_over"] = check_player_death(player, game, SCREEN, font)
            
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
            
            # Invulnerability star
            display_and_check_invulnerability_star(player, SCREEN, game)
            show_star_popup(game, SCREEN)
            
            # GUI
            show_hud(SCREEN, player, font)
            
            player["score"] = score_calculator(player)
            if level_2_condition(trunk, rino, trunk_2, player):
                level_3(player)
            # Refresh screen
            pygame.display.flip()

def level_3(past_player):
    while True:
        # Player
        player = create_player(player_hearts= past_player["hearts"], heart_image= past_player["heart_image"],got_invulnerability_star= past_player["got_invulnerability_star"], stars_count= past_player["stars_count"], inv_star_used=past_player["inv_star_used"])
        
        # Enemy "trunk"
        trunk = create_trunk(4, "left")
        
        # Enemy "trunk 2"
        trunk_2 = create_trunk(5, "right")
        
        # Enemy "rino"
        rino = create_rino(3, "left")
        
        # Enemy "rino 2"
        rino_2 = create_rino(4, "left")
        
        # Enemy "rino_3"
        rino_3 = create_rino(5, "right")
        
        # Map
        platforms = create_level_platforms(3)
        
        # Game
        game = game_flags()

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
                
                keydown_detection(event, player, game, SCREEN, font, platforms)
                # Release keys detection
                keyup_detection(event, player)

            launch_player_events(player, platforms, SCREEN)
            game["game_over"] = check_player_death(player, game, SCREEN, font)
            
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
            
            # GUI
            show_hud(SCREEN, player, font)
            
            player["score"] = score_calculator(player)
            if level_3_condition(trunk, rino, trunk_2, rino_2, rino_3, player):
                level_4(player)
            
            # Refresh screen
            pygame.display.flip()

def level_4(past_player):
    #level4
    while True:
        # Player
        player = create_player(player_hearts= past_player["hearts"], heart_image= past_player["heart_image"],got_invulnerability_star= past_player["got_invulnerability_star"], stars_count= past_player["stars_count"], inv_star_used=past_player["inv_star_used"])
        
        # Enemy "rino"
        rino = create_rino(6, "left")
        
        # Enemy "rino 2"
        rino_2 = create_rino(7, "left")
        
        # Enemy "rino_3"
        rino_3 = create_rino(8, "right")
        
        # Enemy "rino_4"
        rino_4 = create_rino(9, "left")
        
        # Enemy "trunk"
        trunk = create_trunk(6, "left")
        
        # Enemy "trunk 2"
        trunk_2 = create_trunk(7, "right")
        
        # Map
        platforms = create_level_platforms(4)
        
        # Game
        game = game_flags()
        
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
                
                keydown_detection(event, player, game, SCREEN, font, platforms)
                # Release keys detection
                keyup_detection(event, player)

            launch_player_events(player, platforms, SCREEN)
            
            game["game_over"] = check_player_death(player, game, SCREEN, font)
            
            # Showing images and animations
            SCREEN.blit(level_4_background, (0, 0))
            
            #Rino 1 enemy:
            launch_rino_events(rino, player, SCREEN, 6)
            
            #Rino 2 enemy:
            launch_rino_events(rino_2, player, SCREEN, 7)
            
            # Rino 3 enemy
            launch_rino_events(rino_3, player, SCREEN, 8)
            
            # Rino 4 enemy
            launch_rino_events(rino_4, player, SCREEN, 9)
            
            # Trunk 1 enemy
            launch_trunk_events(trunk, player, SCREEN)
            
            # Trunk 2 enemy
            launch_trunk_events(trunk_2, player, SCREEN)
            
            # Player animation
            show_animation(SCREEN, player["animation"], 10, player["hitbox"]["rct"].x, player["hitbox"]["rct"].y)
            
            # Draw the player laser
            launch_drawing_events(player, SCREEN, [trunk, trunk_2], game, font)
            
            artifact_appear_condition(trunk, trunk_2, rino, rino_2, rino_3, SCREEN, player, game)
            
            # GUI
            show_hud(SCREEN, player, font)
            
            player["score"] = score_calculator(player)
            endscreen(game, player, SCREEN, font)
            # Refresh screen
            pygame.display.flip()