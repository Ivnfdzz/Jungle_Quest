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
            
            game["playtime"] = pygame.time.get_ticks()
            
            if level_1_condition(trunk, rino, player):
                level_2(player, game)
            
            SCREEN.blit(player["heart_image"], (HEARTS_GUI_POSITION[0], HEARTS_GUI_POSITION[1]))
            SCREEN.blit(stars_hud, (STARS_POSITION[0], STARS_POSITION[1]))
            show_text(SCREEN, (STARS_POSITION[0] + 80, STARS_POSITION[1] + 25), f"{player["stars_count"]}", font, YELLOW)
            
            # Refresh screen
            pygame.display.flip()

def level_2(past_player, game):
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
        new_playtime = game["playtime"]

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
            
            new_playtime = game["playtime"] + pygame.time.get_ticks()
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
        rino = create_rino(3, "left")
        
        # Enemy "rino 2"
        rino_2 = create_rino(4, "left")
        
        # Enemy "rino_3"
        rino_3 = create_rino(5, "right")
        
        # Map
        platforms = create_level_platforms(3)
        
        # Game
        game = game_flags()
        new_playtime = playtime
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

            launch_player_events(player, platforms, SCREEN)
            
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

def level_4(past_player, playtime):
    #level4
    while True:
        pygame.mixer_music.play()
        # Player
        player = create_player(player_hearts= past_player["hearts"], heart_image= past_player["heart_image"],got_invulnerability_star= past_player["got_invulnerability_star"], stars_count= past_player["stars_count"])
        
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
        new_playtime = playtime
        
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

            launch_player_events(player, platforms, SCREEN)
            
            game["game_over"] = check_player_death(player, game)
            
            # Showing images and animations
            SCREEN.blit(level_4_background, (0, 0))
            
            #Rino enemy:
            launch_rino_events(rino, player, SCREEN, 6)
            
            #Rino enemy:
            launch_rino_events(rino_2, player, SCREEN, 7)
            
            launch_rino_events(rino_3, player, SCREEN, 8)
            
            launch_rino_events(rino_4, player, SCREEN, 9)
            
            launch_trunk_events(trunk, player, SCREEN)
            # Player animation
            
            launch_trunk_events(trunk_2, player, SCREEN)
            
            show_animation(SCREEN, player["animation"], 10, player["hitbox"]["rct"].x, player["hitbox"]["rct"].y)
            
            # Draw the player laser
            launch_drawing_events(player, SCREEN, [trunk, trunk_2], game, font)
            
            get_health_image(player)
            
            
            if not trunk["live"] and not trunk_2["live"] and not rino["live"] and not rino_2["live"] and not rino_3["live"]:
                SCREEN.blit(artifact_image, (ARTIFACT_POSITION[0], ARTIFACT_POSITION[1]))
                if not player["got_artifact"]:
                    if detectar_colision(player["hitbox"]["rct"], player["artifact_rect"]):
                        player["got_artifact"] = True
                        game["show_popup"] = True
                        game["popup_start_time"] = pygame.time.get_ticks()
            
            new_playtime = playtime + pygame.time.get_ticks()
            SCREEN.blit(player["heart_image"], (HEARTS_GUI_POSITION[0], HEARTS_GUI_POSITION[1]))
            SCREEN.blit(stars_hud, (STARS_POSITION[0], STARS_POSITION[1]))
            show_text(SCREEN, (STARS_POSITION[0] + 80, STARS_POSITION[1] + 25), f"{player["stars_count"]}", font, YELLOW)
            
            if game["show_popup"]:
                current_time = pygame.time.get_ticks()
                if current_time - game["popup_start_time"] >= POPUP_DURATION:
                    game["show_popup"] = False
                    quit_game()
                    break 
                else:
                    SCREEN.blit(gameover_popup, (0,0))
            if player["got_artifact"]:
                game["show_popup"] = True
            # Refresh screen
            pygame.display.flip()