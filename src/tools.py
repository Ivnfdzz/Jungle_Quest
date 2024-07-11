import pygame
import sys
from pygame.locals import *
from settings import *
from loads import *
import time

def quit_game():
    pygame.quit()
    sys.exit()

def point_in_rectangle(punto, rect):
    x, y = punto
    return x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom

def detectar_colision(rect_1, rect_2):
    if point_in_rectangle(rect_1.topleft, rect_2) or point_in_rectangle(rect_1.topright, rect_2) or point_in_rectangle(rect_1.bottomleft, rect_2) or point_in_rectangle(rect_1.bottomright, rect_2) or point_in_rectangle(rect_2.topleft, rect_1) or point_in_rectangle(rect_2.topright, rect_1) or point_in_rectangle(rect_2.bottomleft, rect_1) or point_in_rectangle(rect_2.bottomright, rect_1):
        return True
    else:
        return False

def show_text(superficie: pygame.Surface, coordenada: tuple[int, int], texto: str, fuente: pygame.font.Font, color: tuple[int, int, int] = (255, 255, 255), background_color: tuple[int, int, int] = None):
    sup_texto = fuente.render(texto, True, color, background_color)
    rect_texto = sup_texto.get_rect(center = coordenada)
    superficie.blit(sup_texto, rect_texto)
    pygame.display.flip()

def create_block(imagen: pygame.Surface = None, left=0, top=0, width=50, height=50, color=(255, 255, 255), dir=3, borde=0, radio=-1, vel_y=0, on_ground= True, double_jump_used=False):
    if imagen:
        imagen = pygame.transform.scale(imagen, (width, height))
    return {"rct": pygame.Rect(left, top, width, height), "clr": color, "dir": dir, "brd": borde, "rad": radio, "img": imagen, "vel_y": vel_y, "on_ground": on_ground, "double_jump_used": double_jump_used}

def get_animation_direction(right_animation, left_animation, current_direction):
    return right_animation if current_direction == "right" else left_animation

def show_animation(surface, animation, fps, x, y):
    frame = int(time.time() * fps) % len(animation)
    surface.blit(animation[frame], (x, y))

def create_platform(x, y, width, height, color=(0, 255, 0)):
    return {
        "rct": pygame.Rect(x, y, width, height),
        "clr": color,
    }

def create_laser(midRight: tuple[int, int], color: tuple[int, int, int] = (255, 0, 0)):
    block = {"rct": pygame.Rect(0, 0, LASER_WIDTH, LASER_HEIGHT), "color": color, "speed": LASER_SPEED}
    block["rct"].midright = midRight
    return block

def wait_user(key):
    flag_start_up = True
    while flag_start_up:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit_game()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == key:
                    flag_start_up = False

def score_calculator(hearts, playtime, stars):
    match hearts:
        case 5:
            score = stars * 15
        case 4:
            score = stars * 14
        case 3:
            score = stars * 13
        case 2:
            score = stars * 12
        case 1:
            score = stars * 11
    final_score = score, playtime
    return final_score

# Level conditions
def level_1_condition(trunk, rino, player):
    next_lvl = False
    if not trunk["live"] and not rino["live"]:
        if player["hitbox"]["rct"].right >= SCREEN_WIDTH:
            next_lvl = True
        else:
            next_lvl =False
    return next_lvl

def level_2_condition(trunk, rino, trunk_2, player):
    next_lvl = False
    if not trunk["live"] and not rino["live"] and not trunk_2["live"]:
        if player["hitbox"]["rct"].right >= SCREEN_WIDTH:
            next_lvl = True
        else:
            next_lvl = False
    return next_lvl

def level_3_condition(trunk, rino, trunk_2, rino_2, rino_3, player):
    next_lvl = False
    if not trunk["live"] and not rino["live"] and not trunk_2["live"] and not rino_2["live"] and not rino_3["live"]:
        if player["hitbox"]["rct"].right >= SCREEN_WIDTH:
            next_lvl = True
        else:
            next_lvl = False
    return next_lvl

# Platforms
def create_level_platforms(level):
    match level:
        case 1:
            platforms = [
                create_platform(0, SCREEN_HEIGHT - 80, SCREEN_WIDTH, 80, color=GREEN),
                create_platform(290, 330, 115, 20, color=BLUE),
                create_platform(648, 242, 115, 20, color=RED)]
            
        case 2:
            platforms = [
            create_platform(0, SCREEN_HEIGHT - 80, SCREEN_WIDTH, 1, color=GREEN),
            create_platform(0, 117, 148, 1, color=BLUE),
            create_platform(165, 245, 148, 1,  color=BLUE),
            create_platform(324, 373, 480, 1, color=RED)]
            
        case 3:
            platforms = [
            create_platform(0, SCREEN_HEIGHT - 80, SCREEN_WIDTH, 80, color=GREEN),
            create_platform(0, 375, 800, 20, color=BLUE),
            create_platform(653, 193, 147, 20, color=RED),
            create_platform(0, 193, 148, 20, color=RED)]
            
        case 4:
            platforms = [
            create_platform(0, SCREEN_HEIGHT - 80, SCREEN_WIDTH, 80, color=GREEN),
            create_platform(0, 220, 800, 1, color=RED),
            create_platform(0, 370, 800, 1, color=RED)]

    return platforms

# Player
def create_player_block(imagen: pygame.Surface = None):
    return create_block(imagen, PJ_POSITION[0], PJ_POSITION[1], PJ_WIDTH, PJ_HEIGHT, GREEN, 0, 0, vel_y=0, on_ground=True, double_jump_used=False)

def create_player(player_hearts:int=5, heart_image:pygame.Surface= hearts_5, got_invulnerability_star=False, stars_count=0):
    return {
        "hitbox": create_player_block(),
        "hearts": player_hearts,
        "heart_image": heart_image,
        "move_left": False,
        "move_right": False,
        "direction": "right",
        "double_jump_used": False,
        "laser": None,
        "laser_direction": None,
        "shooting": False,
        "shooting_timer": 0,
        "hit_invulnerability": False,
        "hit_invulnerability_start_time": 0,
        "got_invulnerability_star": got_invulnerability_star,
        "invulnerability_star_rect": pygame.Rect(INVULNERABILITY_STAR_POSITION[0], INVULNERABILITY_STAR_POSITION[1], INVULNERABILITY_STAR_SIZE[0], INVULNERABILITY_STAR_SIZE[1]),
        "got_artifact": False,
        "artifact_rect": pygame.Rect(ARTIFACT_POSITION[0], ARTIFACT_POSITION[1], ARTIFACT_SIZE[0], ARTIFACT_SIZE[1]),
        "stars_count": stars_count,
        "on_ground": False,
        "vel_y": 0,
        "animation": None,
        "inv_star_on": False,
        "star_invulnerability_start_time": 0,
        "inv_star_used": False,
        "visual_effect": None,
        "visual_effect_start_time": 0,
        "visual_effect_location": (0, 0)
    }

def handle_player_movement(player):
    if player["move_left"] and not player["move_right"] and player["hitbox"]["rct"].left > 0:
        player["hitbox"]["rct"].x -= PJ_SPEED
        player["direction"] = "left"
    if player["move_right"] and not player["move_left"] and player["hitbox"]["rct"].right < SCREEN_WIDTH:
        player["hitbox"]["rct"].x += PJ_SPEED
        player["direction"] = "right"
    return player["direction"]

def update_player_animation(player):
    if not player["on_ground"]:
        player["animation"] = get_animation_direction(player_jump_right, player_jump_left, player["direction"])
    elif player["shooting"]:
        if player["move_left"] or player["move_right"]:
            player["animation"] = get_animation_direction(player_running_shoot_right, player_running_shoot_left, player["direction"])
        else:
            player["animation"] = get_animation_direction(player_shoot_right, player_shoot_left, player["direction"])
        
        if pygame.time.get_ticks() - player["shooting_timer"] > 200:  
            player["shooting"] = False
    elif player["move_left"] or player["move_right"]:
        player["animation"] = get_animation_direction(player_run_right, player_run_left, player["direction"])
    else:
        player["animation"] = get_animation_direction(player_idle_right, player_idle_left, player["direction"])
    return player["animation"]

def check_player_enviorment_collitions(player, platforms):
    if player["hitbox"]["rct"].bottom >= GROUND_LEVEL:
        player["hitbox"]["rct"].bottom = GROUND_LEVEL
        player["vel_y"] = 0
        player["on_ground"] = True
        player["double_jump_used"] = False
        player["animation"] = get_animation_direction(player_idle_right, player_idle_left, player["direction"])
    else:
        player["on_ground"] = False
        for platform in platforms:
            if player["hitbox"]["rct"].colliderect(platform["rct"]):
                if player["vel_y"] > 0:
                    player["hitbox"]["rct"].bottom = platform["rct"].top
                    player["vel_y"] = 0
                    player["on_ground"] = True
                    player["double_jump_used"] = False
                elif player["vel_y"] == 0:
                    player["hitbox"]["rct"].top = platform["rct"].bottom
                    player["vel_y"] = 0
    return player

def player_gravity(player):
    player["vel_y"] += GRAVITY
    player["hitbox"]["rct"].y += player["vel_y"]

def handle_player_laser(player):
    if player["laser"]:
        if player["laser_direction"] == "right":
            player["laser"]["rct"].x += player["laser"]["speed"]
        else:
            player["laser"]["rct"].x -= player["laser"]["speed"]
        if player["laser"]["rct"].right < 0 or player["laser"]["rct"].left > SCREEN_WIDTH:
            player["laser"] = None

def player_die(player):
    game_over = False
    if player["hearts"] <= 0:
        game_over = True
    return game_over

def player_hit_invulnerability(player):
    if player["hit_invulnerability"] == True:
        current_time = pygame.time.get_ticks()
        if current_time - player["hit_invulnerability_start_time"] > PLAYER_HIT_INVULNERABILITY_DURATION:
            player["hit_invulnerability"] = False

def launch_player_events(player, platforms, screen):
    player_gravity(player)
            
    # Check collision with ground
    check_player_enviorment_collitions(player, platforms)
    
    # Player movement
    handle_player_movement(player)
    
    # Update player animation
    update_player_animation(player)
    
    # Player laser
    handle_player_laser(player)

    # Player hit invulnerability
    player_hit_invulnerability(player)
    
    # Player die
    player_die(player)
    
    #invulnerability star
    show_inv_shield(player, screen)

def key_space_detection(player, game, event):
    if event.key == K_SPACE or event.key == K_UP:
        if game["show_popup"]:
            game["show_popup"] = False
        if player["on_ground"]:
            player["vel_y"] = -JUMP_STRENGTH
            player["on_ground"] = False
        elif not player["double_jump_used"]:
            player["vel_y"] = -JUMP_2_STRENGTH
            player["double_jump_used"] = True

def key_movement_detection(player, event):
    if event.key == K_LEFT or event.key == K_a:
        player["move_left"] = True
        player["direction"] = "left"

    if event.key == K_RIGHT or event.key == K_d:
        player["move_right"] = True
        player["direction"] = "right"

def key_mute_detection(event, game):
    if event.key == K_m:
        if game["playing_music"]:
            pygame.mixer.music.pause()
            game["playing_music"] = False
        else:
            pygame.mixer.music.unpause()
            game["playing_music"] = True
    return game

def key_pause_detection(event, screen, font, game):
    if event.key == K_p:
        pygame.mixer.music.pause()
        show_text(screen, SCREEN_CENTER, "Pause", font, MAGENTA)
        wait_user(K_p)
        if game["playing_music"]:
            pygame.mixer.music.unpause()
        game["in_pause"] = not game["in_pause"]

def key_shoot_detection(player, event):
    if event.key == K_LSHIFT:
        if not player["laser"]:
            player["shooting"] = True
            player["shooting_timer"] = pygame.time.get_ticks()
            player["laser"] = create_laser(player["hitbox"]["rct"].midright if player["direction"] == "right" else player["hitbox"]["rct"].midleft)
            player["laser_direction"] = player["direction"]

def key_inv_star_detection(player, event):
    if event.key == K_x:
        if player["got_invulnerability_star"]:
            if not player["inv_star_used"]:
                player["inv_star_on"] = True
                player["star_invulnerability_start_time"] = pygame.time.get_ticks()
                player["inv_star_used"] = True

def keydown_detection(event, player, game, screen, font):
    if event.type == KEYDOWN:
        # Jumping or skipping pop ups
        key_space_detection(player, game, event)
        
        # Movement
        key_movement_detection(player, event)
        
        # Mute
        game["playing_music"] = key_mute_detection(event, screen)
        
        # Pause
        key_pause_detection(event, screen, font, game)
        
        # Shoot
        key_shoot_detection(player, event)
        
        #inv_star
        key_inv_star_detection(player, event)

def keyup_detection(event, player):
    if event.type == KEYUP:
        if event.key == K_LEFT or event.key == K_a:
            player["move_left"] = False
        if event.key == K_RIGHT or event.key == K_d:
            player["move_right"] = False

def check_player_death(player, game):
    if player["hearts"] <= 0:
        game["game_over"] = True
        return game["game_over"]

def laser_hit_enemy(player, enemy):
    if player["laser"]:
        if detectar_colision(player["laser"]["rct"], enemy["hitbox"]["rct"]):
            enemy["live"] = None
            player["laser"] = None
            player["stars_count"] += 1
            
            player["visual_effect"] = item_feedback
            player["visual_effect_start_time"] = pygame.time.get_ticks()
            player["visual_effect_location"] = (enemy["hitbox"]["rct"].x, enemy["hitbox"]["rct"].y)

def get_health_image(player):
    hearts = player["hearts"]
    match hearts:
        case 5:
            player["heart_image"] = hearts_5
        case 4:
            player["heart_image"] = hearts_4
        case 3:
            player["heart_image"] = hearts_3
        case 2:
            player["heart_image"] = hearts_2
        case 1:
            player["heart_image"] = hearts_1
        case 0:
            player["heart_image"] = hearts_0
    return player["heart_image"]

def display_and_check_invulnerability_star(player, screen, game):
    if not player["got_invulnerability_star"]:
        show_animation(screen, invulnerability_star_animation, 10, INVULNERABILITY_STAR_POSITION[0], INVULNERABILITY_STAR_POSITION[1])
        if detectar_colision(player["hitbox"]["rct"], player["invulnerability_star_rect"]):
            player["got_invulnerability_star"] = True
            game["show_popup"] = True
            game["popup_start_time"] = pygame.time.get_ticks()

def show_inv_shield(player, screen):
    if inv_star_on:
        current_time = pygame.time.get_ticks()
        if current_time - star_invulnerability_start_time < INVULNERABILITY_STAR_DURATION:
            shield_x = player["hitbox"]["rct"].centerx - inv_star_shield.get_width() // 2
            shield_y = player["hitbox"]["rct"].centery - inv_star_shield.get_height() // 2
            screen.blit(inv_star_shield, (shield_x, shield_y))
        else:
            inv_star_on = False
            star_invulnerability_start_time = None

#Rino
def create_rino_block(level:str):
    return create_block(left=RINO_POS_AND_LIMIT[f"{level}"]["position"][0], top=RINO_POS_AND_LIMIT[f"{level}"]["position"][1], width=RINO_WIDTH, height=RINO_HEIGHT)

def create_rino(number, rino_direction):
    return {
    "hitbox": create_rino_block(number),
    "live": True,
    "direction": rino_direction,
    "animation": None
    }

def handle_rino_movement(rino, number):
    if rino["direction"] == "left":
        rino["hitbox"]["rct"].x -= RINO_SPEED
        rino["animation"] = rino_run_right
        if rino["hitbox"]["rct"].left <= RINO_POS_AND_LIMIT[f"{number}"]["limit"]:
            rino["direction"] = "right"
    else:
        rino["hitbox"]["rct"].x += RINO_SPEED
        rino["animation"] = rino_run_left
        if rino["hitbox"]["rct"].right >= SCREEN_WIDTH:
            rino["direction"] = "left"

def rino_hit_player(player, rino):
    if not player["inv_star_on"]:
        if not player["hit_invulnerability"]:
            if detectar_colision(player["hitbox"]["rct"], rino["hitbox"]["rct"]):
                player["hearts"] -= 1
                if rino["direction"] == "left":
                    player["hitbox"]["rct"].x += 20
                else:
                    player["hitbox"]["rct"].x -= 20
                player["vel_y"] = -JUMP_STRENGTH + 5 
                player["hit_invulnerability"] = True
                player["hit_invulnerability_start_time"] = pygame.time.get_ticks()

def launch_rino_events(rino, player, screen, number):
    if rino["live"]:
        handle_rino_movement(rino, number)
        rino_hit_player(rino, player)
        laser_hit_enemy(player, rino)
        show_animation(screen, rino["animation"], 10, rino["hitbox"]["rct"].x, rino["hitbox"]["rct"].y)

#Trunk
def create_trunk_block(level:str):
    return create_block(left=TRUNK_POS_AND_VISION[f"{level}"]["position"][0], top=TRUNK_POS_AND_VISION[f"{level}"]["position"][1], width=TRUNK_WIDTH, height=TRUNK_HEIGHT)

def create_trunk(level, direction):
    return{
    "hitbox": create_trunk_block(level),
    "animation": None,
    "bullet": None,
    "live": True,
    "vision": create_platform(TRUNK_POS_AND_VISION[f"{level}"]["vision"]["x"], TRUNK_POS_AND_VISION[f"{level}"]["vision"]["y"], TRUNK_POS_AND_VISION[f"{level}"]["vision"]["width"], TRUNK_POS_AND_VISION[f"{level}"]["vision"]["height"], color=RED),
    "last_shoot_time": 0,
    "direction": direction
    }

def trunk_sees_player(player, trunk):
    # Player collide with trunks vision
    if detectar_colision(player["hitbox"]["rct"], trunk["vision"]["rct"]):
        trunk["animation"] = trunk_attack_right
        # Setting a time between each trunk's shoot and creating the shoot
        if pygame.time.get_ticks() - trunk["last_shoot_time"] > TRUNK_SHOOT_TIME:
            trunk["last_shoot_time"] = pygame.time.get_ticks()
            if trunk["direction"] == "left":
                trunk["bullet"] = create_laser(trunk["hitbox"]["rct"].midleft, color=YELLOW)
            else:
                trunk["bullet"] = create_laser(trunk["hitbox"]["rct"].midright, color=YELLOW)
        return True
    return False

def trunk_shooting(trunk, player):
    # Trunk shoot movement
    if trunk["bullet"]:
        if trunk["direction"] == "left":
            trunk["bullet"]["rct"].x -= trunk["bullet"]["speed"]
        else:
            trunk["bullet"]["rct"].x += trunk["bullet"]["speed"]
            
    # Trunk shoot hit player
    if not player["inv_star_on"]:
        if not player["hit_invulnerability"]:
            if detectar_colision(player["hitbox"]["rct"], trunk["bullet"]["rct"]):
                player["hearts"] -= 1
                trunk["bullet"] = None
    # No interatction with player
    else:
        trunk["animation"] = get_animation_direction(trunk_idle_left, trunk_idle_right, trunk["direction"])

def launch_trunk_events(trunk, player, screen) :
    if trunk["live"]:
        laser_hit_enemy(player, trunk)
        player_in_vision = trunk_sees_player(player, trunk)
        trunk_shooting(trunk, player)
        
        if player_in_vision:
            trunk["animation"] = get_animation_direction(trunk_attack_left, trunk_attack_right, trunk["direction"])
        else:
            trunk["animation"] = get_animation_direction(trunk_idle_left, trunk_idle_right, trunk["direction"])
        
        show_animation(screen, trunk["animation"], 10, trunk["hitbox"]["rct"].x, trunk["hitbox"]["rct"].y)

# Drawing
def handle_visual_effects(player, screen):
    if player["visual_effect"]:
        current_time = pygame.time.get_ticks()
        if current_time - player["visual_effect_start_time"] < VISUAL_EFFECT_DURATION:
            frame = (current_time - player["visual_effect_start_time"]) // 75  # 75ms per frame
            if frame < len(player["visual_effect"]):
                screen.blit(player["visual_effect"][frame], player["visual_effect_location"])
            else:
                player["visual_effect"] = None
        else:
            player["visual_effect"] = None

def player_laser_drawing(player, screen):
    if player["laser"]:
        pygame.draw.rect(screen, player["laser"]["color"], player["laser"]["rct"])

def trunk_bullet_drawing(trunk, screen):
    if trunk["bullet"]:
        if not trunk["live"]:
            trunk["bullet"] = None
        else:
            pygame.draw.rect(screen, trunk["bullet"]["color"], trunk["bullet"]["rct"])

def mute_drawing(game, screen, font):
    if not game["playing_music"]:
        show_text(screen, MUTE_TEXT_POS, "Mute", font, GREEN)

def launch_drawing_events(player, screen, trunks, playing_music, font):
    player_laser_drawing(player, screen)
    handle_visual_effects(player, screen)
    mute_drawing(playing_music, screen, font)
    if isinstance(trunks, list):
        for trunk in trunks:
            trunk_bullet_drawing(trunk, screen)
    else:
        trunk_bullet_drawing(trunks, screen)

# Mix
def game_flags():
    return {
    "playing_music": True,
    "in_pause": False,
    "show_popup": True,
    "playtime": 0,
    "game_over": False,
    "popup_start_time": 0
    }

def show_star_popup(game, screen):
    if game["show_popup"]:
        current_time = pygame.time.get_ticks()
        if current_time - game["popup_start_time"] >= POPUP_DURATION:
            game["show_popup"] = False
        else:
            screen.blit(popup_inv_star, (0,0))

