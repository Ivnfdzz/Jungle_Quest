import pygame
import sys
import csv
from pygame.locals import *
from settings import *
from loads import *
import time

def quit_game():
    """Quits the game and exits the program.
    """
    pygame.quit()
    sys.exit()

def point_in_rectangle(punto:tuple, rect:pygame.Rect)-> bool:
    """Checks if a point is inside a rectangle.

    Args:
    punto (tuple): The (x, y) coordinates of the point.
    rect (pygame.Rect): The rectangle to check.

    Returns:
    bool: True if the point is inside the rectangle, False otherwise.
    """
    x, y = punto
    return x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom

def detect_collition(rect_1:pygame.Rect, rect_2:pygame.Rect)-> bool:
    """DEL PROFE
    Detects collision between two rectangles.

    Args:
    rect_1 (pygame.Rect): The first rectangle.
    rect_2 (pygame.Rect): The second rectangle.

    Returns:
    bool: True if the rectangles collide, False otherwise.
    """
    if point_in_rectangle(rect_1.topleft, rect_2) or point_in_rectangle(rect_1.topright, rect_2) or point_in_rectangle(rect_1.bottomleft, rect_2) or point_in_rectangle(rect_1.bottomright, rect_2) or point_in_rectangle(rect_2.topleft, rect_1) or point_in_rectangle(rect_2.topright, rect_1) or point_in_rectangle(rect_2.bottomleft, rect_1) or point_in_rectangle(rect_2.bottomright, rect_1):
        return True
    else:
        return False

def show_text(superficie: pygame.Surface, coordenada: tuple[int, int], texto: str, fuente: pygame.font.Font, color: tuple[int, int, int] = (255, 255, 255), background_color: tuple[int, int, int] = None)-> None:
    """DEL PROFE:
    Displays text on a surface.

    Args:
    superficie (pygame.Surface): The surface to draw on.
    coordenada (tuple[int, int]): The (x, y) coordinates for the text center.
    texto (str): The text to display.
    fuente (pygame.font.Font): The font to use.
    color (tuple[int, int, int], optional): The color of the text. Defaults to white.
    background_color (tuple[int, int, int], optional): The background color. Defaults to None.
    """
    sup_texto = fuente.render(texto, True, color, background_color)
    rect_texto = sup_texto.get_rect(center = coordenada)
    superficie.blit(sup_texto, rect_texto)
    pygame.display.flip()

def create_block(left=0, top=0, width=50, height=50, color=(255, 255, 255), dir=3, borde=0, radio=-1, vel_y=0, on_ground= True, double_jump_used=False)-> dict:
    """DEL PROFE:
    Creates a block with specified properties.

    Args:
    imagen (pygame.Surface, optional): The image for the block. Defaults to None.
    left (int, optional): The left coordinate. Defaults to 0.
    top (int, optional): The top coordinate. Defaults to 0.
    width (int, optional): The width of the block. Defaults to 50.
    height (int, optional): The height of the block. Defaults to 50.
    color (tuple[int, int, int], optional): The color of the block. Defaults to white.
    dir (int, optional): The direction of the block. Defaults to 3.
    borde (int, optional): The border width. Defaults to 0.
    radio (int, optional): The radius for rounded corners. Defaults to -1.
    vel_y (int, optional): The vertical velocity. Defaults to 0.
    on_ground (bool, optional): Whether the block is on the ground. Defaults to True.
    double_jump_used (bool, optional): Whether double jump has been used. Defaults to False.

    Returns:
    dict: A dictionary containing the block's properties.
    """

    return {"rct": pygame.Rect(left, top, width, height), "clr": color, "dir": dir, "brd": borde, "rad": radio, "vel_y": vel_y, "on_ground": on_ground, "double_jump_used": double_jump_used}

def get_animation_direction(right_animation:list, left_animation:list, current_direction:str)-> list:
    """Returns the appropriate animation based on the current direction.

    Args:
    right_animation: The animation for right direction.
    left_animation: The animation for left direction.
    current_direction (str): The current direction ('right' or 'left').

    Returns:
    The appropriate animation for the current direction.
    """
    return right_animation if current_direction == "right" else left_animation

def show_animation(surface:pygame.Surface, animation:list, fps:int, x:int, y:int)-> None:
    """Displays an animation on the surface.

    Args:
    surface (pygame.Surface): The surface to draw on.
    animation: The animation to display.
    fps (int): The frames per second for the animation.
    x (int): The x-coordinate to display the animation.
    y (int): The y-coordinate to display the animation.
    """
    frame = int(time.time() * fps) % len(animation)
    surface.blit(animation[frame], (x, y))

def create_platform(x:int, y:int, width:int, height:int, color:tuple=(0, 255, 0))-> dict:
    """Creates a platform with specified properties.

    Args:
    x (int): The x-coordinate of the platform.
    y (int): The y-coordinate of the platform.
    width (int): The width of the platform.
    height (int): The height of the platform.
    color (tuple[int, int, int], optional): The color of the platform. Defaults to green.

    Returns:
    dict: A dictionary containing the platform's properties.
    """
    return {
        "rct": pygame.Rect(x, y, width, height),
        "clr": color,
    }

def create_laser(midRight: tuple[int, int], color: tuple[int, int, int] = (255, 0, 0))-> dict:
    """Creates a laser with specified properties.

    Args:
    midRight (tuple[int, int]): The midright coordinates of the laser.
    color (tuple[int, int, int], optional): The color of the laser. Defaults to red.

    Returns:
    dict: A dictionary containing the laser's properties.
    """
    block = {"rct": pygame.Rect(0, 0, LASER_WIDTH, LASER_HEIGHT), "color": color, "speed": LASER_SPEED}
    block["rct"].midright = midRight
    return block

def wait_user(key)-> None:
    """DEL PROFE:
    Waits for the user to press a specific key.

    Args:
    key: The key to wait for.
    """
    flag_start_up = True
    while flag_start_up:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit_game()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == key:
                    flag_start_up = False

# Level conditions
def level_1_condition(trunk:dict, rino:dict, player:dict)-> bool:
    """ Checks the condition for completing level 1.

    Args:
    trunk: The trunk enemy.
    rino: The rino enemy.
    player: The player object.

    Returns:
    bool: True if the level is completed, False otherwise.
    """
    next_lvl = False
    if not trunk["live"] and not rino["live"]:
        if player["hitbox"]["rct"].right >= SCREEN_WIDTH:
            next_lvl = True
        else:
            next_lvl =False
    return next_lvl

def level_2_condition(trunk:dict, rino:dict, trunk_2:dict, player:dict)-> bool:
    """Checks the condition for completing level 2.

    Args:
    trunk: The first trunk enemy.
    rino: The rino enemy.
    trunk_2: The second trunk enemy.
    player: The player object.

    Returns:
    bool: True if the level is completed, False otherwise.
    """
    next_lvl = False
    if not trunk["live"] and not rino["live"] and not trunk_2["live"]:
        if player["hitbox"]["rct"].right >= SCREEN_WIDTH:
            next_lvl = True
        else:
            next_lvl = False
    return next_lvl

def level_3_condition(trunk:dict, rino:dict, trunk_2:dict, rino_2:dict, rino_3:dict, player:dict)-> bool:
    """Checks the condition for completing level 3.

    Args:
    trunk: The first trunk enemy.
    rino: The first rino enemy.
    trunk_2: The second trunk enemy.
    rino_2: The second rino enemy.
    rino_3: The third rino enemy.
    player: The player object.

    Returns:
    bool: True if the level is completed, False otherwise.
    """
    next_lvl = False
    if not trunk["live"] and not rino["live"] and not trunk_2["live"] and not rino_2["live"] and not rino_3["live"]:
        if player["hitbox"]["rct"].right >= SCREEN_WIDTH:
            next_lvl = True
        else:
            next_lvl = False
    return next_lvl

# Platforms
def create_level_platforms(level:int)-> list:
    """Creates platforms for a specific level.

    Args:
    level (int): The level number.

    Returns:
    list: A list of platform dictionaries for the specified level.
    """
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
def create_player_block()-> dict:
    """Creates a player block.

    Returns:
    dict: A dictionary containing the player block's properties.
    """
    return create_block(PJ_POSITION[0], PJ_POSITION[1], PJ_WIDTH, PJ_HEIGHT, GREEN, 0, 0, vel_y=0, on_ground=True, double_jump_used=False)

def create_player(player_hearts:int=5, heart_image:pygame.Surface= hearts_5, got_invulnerability_star:bool=False, stars_count:int=0, inv_star_used:bool= False)-> dict:
    """ Creates a player with specified properties.

    Args:
    player_hearts (int, optional): The number of hearts the player has. Defaults to 5.
    heart_image (pygame.Surface, optional): The image for the player's hearts. Defaults to hearts_5.
    got_invulnerability_star (bool, optional): Whether the player has the invulnerability star. Defaults to False.
    stars_count (int, optional): The number of stars collected. Defaults to 0.
    inv_star_used (bool, optional): Whether the invulnerability star has been used. Defaults to False.

    Returns:
    dict: A dictionary containing the player's properties.
    """
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
        "inv_star_used": inv_star_used,
        "visual_effect": None,
        "visual_effect_start_time": 0,
        "visual_effect_location": (0, 0)
    }

def handle_player_movement(player:dict)->str:
    """Handles the player's movement.

    Args:
    player (dict): The player object.

    Returns:
    str: The current direction of the player ('left' or 'right').
    """
    if player["move_left"] and not player["move_right"] and player["hitbox"]["rct"].left > 0:
        player["hitbox"]["rct"].x -= PJ_SPEED
        player["direction"] = "left"
    if player["move_right"] and not player["move_left"] and player["hitbox"]["rct"].right < SCREEN_WIDTH:
        player["hitbox"]["rct"].x += PJ_SPEED
        player["direction"] = "right"
    return player["direction"]

def update_player_animation(player:dict)-> list:
    """Updates the player's animation based on their current state.

    Args:
    player (dict): The player object.

    Returns:
    The updated animation for the player.
    """
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

def check_player_enviorment_collitions(player:dict, platforms:list)-> dict:
    """Checks for collisions between the player and the environment.

    Args:
    player (dict): The player object.
    platforms (list): A list of platform objects.

    Returns:
    dict: The updated player object.
    """
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

def player_gravity(player:dict)-> None:
    """Applies gravity to the player.

    Args:
    player (dict): The player object.
    """
    player["vel_y"] += GRAVITY
    player["hitbox"]["rct"].y += player["vel_y"]

def handle_player_laser(player:dict)-> None:
    """Handles the player's laser movement and removal.

    Args:
    player (dict): The player object.
    """
    if player["laser"]:
        if player["laser_direction"] == "right":
            player["laser"]["rct"].x += player["laser"]["speed"]
        else:
            player["laser"]["rct"].x -= player["laser"]["speed"]
        if player["laser"]["rct"].right < 0 or player["laser"]["rct"].left > SCREEN_WIDTH:
            player["laser"] = None

def player_die(player:dict)-> bool:
    """
    Checks if the player has died.

    Args:
    player (dict): The player object.

    Returns:
    bool: True if the player has died, False otherwise.
    """
    game_over = False
    if player["hearts"] <= 0:
        game_over = True
    return game_over

def player_hit_invulnerability(player:dict)-> None:
    """Handles the player's invulnerability after being hit.

    Args:
    player (dict): The player object.
    """
    if player["hit_invulnerability"] == True:
        current_time = pygame.time.get_ticks()
        if current_time - player["hit_invulnerability_start_time"] > PLAYER_HIT_INVULNERABILITY_DURATION:
            player["hit_invulnerability"] = False

def handle_drop_through_platform(player: dict, platforms: list) -> None:
    """Allows the player to drop through platforms when pressing 's'.

    Args:
    player (dict): The player object.
    platforms (list): A list of platform objects.
    """
    for platform in platforms:
        if (player["hitbox"]["rct"].bottom == platform["rct"].top and
            player["hitbox"]["rct"].right > platform["rct"].left and
            player["hitbox"]["rct"].left < platform["rct"].right):
            if platform["rct"].bottom < GROUND_LEVEL:
                player["hitbox"]["rct"].top = platform["rct"].bottom
                player["vel_y"] = 1
                player["on_ground"] = False
                break

def launch_player_events(player:dict, platforms:list, screen:pygame.Surface)-> None:
    """Launches all player-related events.

    Args:
    player (dict): The player object.
    platforms (list): A list of platform objects.
    screen (pygame.Surface): The game screen.
    """

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

def key_space_detection(player:dict, game:dict, event:pygame.event)-> None:
    """Handles space key events for jumping and popup dismissal.

    Args:
    player (dict): The player object.
    game (dict): The game object.
    event (pygame.event.Event): The key event.
    """
    if event.key == K_SPACE or event.key == K_UP:
        if game["show_popup"]:
            game["show_popup"] = False
        if player["on_ground"]:
            player["vel_y"] = -JUMP_STRENGTH
            player_jump_sound.play()
            player["on_ground"] = False
        elif not player["double_jump_used"]:
            player["vel_y"] = -JUMP_2_STRENGTH
            player["double_jump_used"] = True
            player_jump_sound.play()

def key_movement_detection(player: dict, event: pygame.event, platforms: list) -> None:
    """Handles movement key events.

    Args:
    player (dict): The player object.
    event (pygame.event.Event): The key event.
    platforms (list): A list of platform objects.
    """
    if event.key == K_a:
        player["move_left"] = True
        player["direction"] = "left"
    if event.key == K_d:
        player["move_right"] = True
        player["direction"] = "right"
    if event.key == K_s:
        handle_drop_through_platform(player, platforms)

def key_mute_detection(event:pygame.event, game:dict)-> None:
    """Handles mute key events.

    Args:
    event (pygame.event.Event): The key event.
    game (dict): The game object.
    """
    if event.key == K_m:
        if game["playing_music"]:
            pygame.mixer.music.pause()
            game["playing_music"] = False
        else:
            pygame.mixer.music.unpause()
            game["playing_music"] = True

def key_pause_detection(event:pygame.event, screen:pygame.Surface, font:pygame.font, game:dict)-> None:
    """Handles pause key events.

    Args:
    event (pygame.event): The key event.
    screen (pygame.Surface): The game screen.
    font (pygame.font.Font): The font to use for text.
    game (dict): The game object.
    """
    if event.key == K_p:
        pygame.mixer.music.pause()
        show_text(screen, SCREEN_CENTER, "Pause", font, GREEN)
        wait_user(K_p)
        if game["playing_music"]:
            pygame.mixer.music.unpause()
        game["in_pause"] = not game["in_pause"]

def key_shoot_detection(player:dict, event:pygame.event)-> None:
    """Handles shoot key events.

    Args:
    player (dict): The player object.
    event (pygame.event): The key event.
    """
    if event.key == K_LSHIFT:
        if not player["laser"]:
            player["shooting"] = True
            player["shooting_timer"] = pygame.time.get_ticks()
            player["laser"] = create_laser(player["hitbox"]["rct"].midright if player["direction"] == "right" else player["hitbox"]["rct"].midleft)
            player["laser_direction"] = player["direction"]
            player_laser_sound.play()

def key_inv_star_detection(player:dict, event:pygame.event)-> None:
    """Handles invulnerability star key events.

    Args:
    player (dict): The player object.
    event (pygame.event): The key event.
    """
    if event.key == K_x:
        if player["got_invulnerability_star"]:
            if not player["inv_star_used"]:
                player["inv_star_on"] = True
                player["star_invulnerability_start_time"] = pygame.time.get_ticks()
                player["inv_star_used"] = True
                inv_star_use_sound.play()

def keydown_detection(event:pygame.event, player:dict, game:dict, screen:pygame.Surface, font:pygame.font, platforms:pygame.Rect)-> None:
    """Handles all keydown events.

    Args:
    event (pygame.event): The key event.
    player (dict): The player object.
    game (dict): The game object.
    screen (pygame.Surface): The game screen.
    font (pygame.font): The font to use for text.
    platforms (pygame.Rect): The game platforms
    """
    if event.type == KEYDOWN:
        # Jumping or skipping pop ups
        key_space_detection(player, game, event)
        
        # Movement
        key_movement_detection(player, event, platforms)
        
        # Mute
        key_mute_detection(event, game)
        
        # Pause
        key_pause_detection(event, screen, font, game)
        
        # Shoot
        key_shoot_detection(player, event)
        
        #inv_star
        key_inv_star_detection(player, event)
        

def keyup_detection(event:pygame.event, player:dict)-> None:
    """Handles all keyup events.

    Args:
    event (pygame.event): The key event.
    player (dict): The player object.
    """
    if event.type == KEYUP:
        if event.key == K_LEFT or event.key == K_a:
            player["move_left"] = False
        if event.key == K_RIGHT or event.key == K_d:
            player["move_right"] = False

def check_player_death(player:dict, game:dict, screen:pygame.Surface, font:pygame.font):
    """Checks if the player has died and handles game over.

    Args:
    player (dict): The player object.
    game (dict): The game object.
    screen (pygame.Surface): The game screen
    font (pygame.font): The game font

    Returns:
    bool: True if the game is over, False otherwise.
    """
    if player["hearts"] <= 0:
        game["game_over"] = True
        player["name"] = get_player_name(screen, font)
        save_score(player)
        return game["game_over"]
    return False


def laser_hit_enemy(player:dict, enemy:dict)-> None:
    """Handles laser hits on enemies.

    Args:
    player (dict): The player object.
    enemy (dict): The enemy object.
    """
    try:
        if player["laser"]:
            if detect_collition(player["laser"]["rct"], enemy["hitbox"]["rct"]):
                enemy["live"] = None
                player["laser"] = None
                player["stars_count"] += 1
                enemy_killed_sound.play()
                player["visual_effect"] = item_feedback
                player["visual_effect_start_time"] = pygame.time.get_ticks()
                player["visual_effect_location"] = (enemy["hitbox"]["rct"].x, enemy["hitbox"]["rct"].y)
    except KeyError as e:
        print(f"KeyError: Missing key {e} in player or enemy dictionary")

def get_health_image(player:dict)-> pygame.Surface:
    """Gets the appropriate health image based on the player's hearts.

    Args:
    player (dict): The player object.

    Returns:
    pygame.Surface: The health image to display.
    """
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

def display_and_check_invulnerability_star(player:dict, screen:pygame.Surface, game:dict)-> None:
    """Displays the invulnerability star and checks if the player has collected it.

    Args:
    player (dict): The player object.
    screen (pygame.Surface): The game screen.
    game (dict): The game object.
    """
    if not player["got_invulnerability_star"]:
        show_animation(screen, invulnerability_star_animation, 10, INVULNERABILITY_STAR_POSITION[0], INVULNERABILITY_STAR_POSITION[1])
        if detect_collition(player["hitbox"]["rct"], player["invulnerability_star_rect"]):
            player["got_invulnerability_star"] = True
            game["show_popup"] = True
            game["popup_start_time"] = pygame.time.get_ticks()

def show_inv_shield(player:dict, screen:pygame.Surface)-> None:
    """Displays the invulnerability shield around the player.

    Args:
    player (dict): The player object.
    screen (pygame.Surface): The game screen.
    """
    if player["inv_star_on"]:
        current_time = pygame.time.get_ticks()
        if current_time - player["star_invulnerability_start_time"] < INVULNERABILITY_STAR_DURATION:
            shield_x = player["hitbox"]["rct"].centerx - inv_star_shield.get_width() // 2
            shield_y = player["hitbox"]["rct"].centery - inv_star_shield.get_height() // 2
            screen.blit(inv_star_shield, (shield_x, shield_y))
        else:
            player["inv_star_on"] = False
            player["star_invulnerability_start_time"] = None
            player["inv_star_used"] = True

#Rino
def create_rino_block(level:str)-> dict:
    """Creates a rino block for a specific level.

    Args:
    level (str): The level identifier.

    Returns:
    dict: A dictionary containing the rino block's properties.
    """
    return create_block(left=RINO_POS_AND_LIMIT[f"{level}"]["position"][0], top=RINO_POS_AND_LIMIT[f"{level}"]["position"][1], width=RINO_WIDTH, height=RINO_HEIGHT)

def create_rino(number:str, rino_direction:str)-> dict:
    """Creates a rino enemy.

    Args:
    number (str): The rino identifier.
    rino_direction (str): The initial direction of the rino.

    Returns:
    dict: A dictionary containing the rino's properties.
    """
    return {
    "hitbox": create_rino_block(number),
    "live": True,
    "direction": rino_direction,
    "animation": None
    }

def handle_rino_movement(rino:dict, number:str)-> None:
    """Handles the rino's movement.

    Args:
    rino (dict): The rino object.
    number (str): The rino identifier.
    """
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

def rino_hit_player(player:dict, rino:dict)-> None:
    """Handles collisions between the rino and the player.

    Args:
    player (dict): The player object.
    rino (dict): The rino object.
    """
    if not player["inv_star_on"]:
        if not player["hit_invulnerability"]:
            if detect_collition(player["hitbox"]["rct"], rino["hitbox"]["rct"]):
                player["hearts"] -= 1
                rino_hit_player_sound.play()
                if rino["direction"] == "left":
                    player["hitbox"]["rct"].x += 20
                else:
                    player["hitbox"]["rct"].x -= 20
                player["vel_y"] = -JUMP_STRENGTH + 5 
                player["hit_invulnerability"] = True
                player["hit_invulnerability_start_time"] = pygame.time.get_ticks()

def launch_rino_events(rino:dict, player:dict, screen:pygame.Surface, number:str)-> None:
    """Launches all rino-related events.

    Args:
    rino (dict): The rino object.
    player (dict): The player object.
    screen (pygame.Surface): The game screen.
    number (str): The rino identifier.
    """
    if rino["live"]:
        handle_rino_movement(rino, number)
        rino_hit_player(player, rino)
        laser_hit_enemy(player, rino)
        show_animation(screen, rino["animation"], 10, rino["hitbox"]["rct"].x, rino["hitbox"]["rct"].y)

#Trunk
def create_trunk_block(level:str)-> dict:
    """Creates a trunk block for a specific level.

    Args:
    level (str): The level identifier.

    Returns:
    dict: A dictionary containing the trunk block's properties.
    """
    return create_block(left=TRUNK_POS_AND_VISION[f"{level}"]["position"][0], top=TRUNK_POS_AND_VISION[f"{level}"]["position"][1], width=TRUNK_WIDTH, height=TRUNK_HEIGHT)

def create_trunk(level:str, direction:str)-> dict:
    """Creates a trunk enemy.

    Args:
    level (str): The level identifier.
    direction (str): The initial direction of the trunk.

    Returns:
    dict: A dictionary containing the trunk's properties.
    """
    return{
    "hitbox": create_trunk_block(level),
    "animation": None,
    "bullet": None,
    "live": True,
    "vision": create_platform(TRUNK_POS_AND_VISION[f"{level}"]["vision"]["x"], TRUNK_POS_AND_VISION[f"{level}"]["vision"]["y"], TRUNK_POS_AND_VISION[f"{level}"]["vision"]["width"], TRUNK_POS_AND_VISION[f"{level}"]["vision"]["height"], color=RED),
    "last_shoot_time": 0,
    "direction": direction
    }

def trunk_sees_player(player:dict, trunk:dict)-> bool:
    """Checks if the trunk sees the player and handles shooting.

    Args:
    player (dict): The player object.
    trunk (dict): The trunk object.

    Returns:
    bool: True if the trunk sees the player, False otherwise.
    """
    # Player collide with trunks vision
    if detect_collition(player["hitbox"]["rct"], trunk["vision"]["rct"]):
        trunk["animation"] = trunk_attack_right
        # Setting a time between each trunk's shoot and creating the shoot
        if pygame.time.get_ticks() - trunk["last_shoot_time"] > TRUNK_SHOOT_TIME:
            trunk["last_shoot_time"] = pygame.time.get_ticks()
            trunk_shoot_sound.play()
            if trunk["direction"] == "left":
                trunk["bullet"] = create_laser(trunk["hitbox"]["rct"].midleft, color=YELLOW)
            else:
                trunk["bullet"] = create_laser(trunk["hitbox"]["rct"].midright, color=YELLOW)
        return True
    return False

def trunk_shooting(trunk:dict, player:dict)-> None:
    """Handles the trunk's shooting behavior.

    Args:
    trunk (dict): The trunk object.
    player (dict): The player object.
    """
    # Trunk shoot movement
    if trunk["bullet"]:
        if trunk["direction"] == "left":
            trunk["bullet"]["rct"].x -= trunk["bullet"]["speed"]
        else:
            trunk["bullet"]["rct"].x += trunk["bullet"]["speed"]
        
        # Trunk shoot hit player
        if not player["inv_star_on"] and not player["hit_invulnerability"]:
            if detect_collition(player["hitbox"]["rct"], trunk["bullet"]["rct"]):
                player["hearts"] -= 1
                player_hit_sound.play()
                trunk["bullet"] = None
                return
        
        # Remove bullet if it goes off screen
        if trunk["bullet"]["rct"].right < 0 or trunk["bullet"]["rct"].left > SCREEN_WIDTH:
            trunk["bullet"] = None
    
    # Set animation if there's no bullet
    if not trunk["bullet"]:
        trunk["animation"] = get_animation_direction(trunk_idle_left, trunk_idle_right, trunk["direction"])

def launch_trunk_events(trunk:dict, player:dict, screen:pygame.Surface)-> None:
    """Launches all trunk-related events.

    Args:
    trunk (dict): The trunk object.
    player (dict): The player object.
    screen (pygame.Surface): The game screen.
    """
    if trunk["live"]:
        laser_hit_enemy(player, trunk)
        player_in_vision = trunk_sees_player(player, trunk)
        trunk_shooting(trunk, player)
        
        if player_in_vision:
            trunk["animation"] = get_animation_direction(trunk_attack_left, trunk_attack_right, trunk["direction"])
        else:
            trunk["animation"] = get_animation_direction(trunk_idle_left, trunk_idle_right, trunk["direction"])
        
        show_animation(screen, trunk["animation"], 10, trunk["hitbox"]["rct"].x, trunk["hitbox"]["rct"].y)
    else:
        trunk["bullet"] = None

# Drawing
def handle_visual_effects(player:dict, screen:pygame.Surface)-> None:
    """Handles visual effects for the player.

    Args:
    player (dict): The player object.
    screen (pygame.Surface): The game screen.
    """

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

def player_laser_drawing(player:dict, screen:pygame.Surface)-> None:
    """Draws the player's laser on the screen.

    Args:
    player (dict): The player object.
    screen (pygame.Surface): The game screen.
    """
    if player["laser"]:
        pygame.draw.rect(screen, player["laser"]["color"], player["laser"]["rct"])

def trunk_bullet_drawing(trunk:dict, screen:pygame.Surface)-> None:
    """Draws the trunk's bullet on the screen.

    Args:
    trunk (dict): The trunk object.
    screen (pygame.Surface): The game screen.
    """
    if trunk["bullet"]:
        if not trunk["live"]:
            trunk["bullet"] = None
        else:
            pygame.draw.rect(screen, trunk["bullet"]["color"], trunk["bullet"]["rct"])

def mute_drawing(game:dict, screen:pygame.Surface, font:pygame.font)-> None:
    """Draws the mute text on the screen when the game is muted.

    Args:
    game (dict): The game object.
    screen (pygame.Surface): The game screen.
    font (pygame.font.Font): The font to use for the mute text.
    """
    if not game["playing_music"]:
        show_text(screen, MUTE_TEXT_POS, "Mute", font, GREEN)

def launch_drawing_events(player:dict, screen:pygame.Surface, trunks:list, playing_music:bool, font:pygame.font)-> None:
    """Launches all drawing-related events.

    Args:
    player (dict): The player object.
    screen (pygame.Surface): The game screen.
    trunks (list): The trunk object(s).
    playing_music (bool): Whether music is currently playing.
    font (pygame.font.Font): The font to use for text.
    """
    player_laser_drawing(player, screen)
    handle_visual_effects(player, screen)
    mute_drawing(playing_music, screen, font)
    show_inv_shield(player, screen)
    if isinstance(trunks, list):
        for trunk in trunks:
            trunk_bullet_drawing(trunk, screen)
    else:
        trunk_bullet_drawing(trunks, screen)

# Mix
def game_flags()-> dict:
    """Creates and returns a dictionary of game flags.

    Returns:
    dict: A dictionary containing various game flags and their initial values.
    """
    return {
    "playing_music": True,
    "in_pause": False,
    "show_popup": False,
    "playtime": 0,
    "game_over": False,
    "popup_start_time": 0,
    "sound_played": False
    }

def show_star_popup(game:dict, screen:pygame.Surface)-> None:
    """Displays the invulnerability star popup.

    Args:
    game (dict): The game object.
    screen (pygame.Surface): The game screen.
    """
    if game["show_popup"]:
        current_time = pygame.time.get_ticks()
        if current_time - game["popup_start_time"] >= POPUP_DURATION:
            game["show_popup"] = False
            game["sound_played"] = False
        else:
            screen.blit(popup_inv_star, (0,0))
            if not game["sound_played"]:
                inv_star_popup_sound.play()
                game["sound_played"] = True

def artifact_appear_condition(trunk:dict, trunk_2:dict, rino:dict, rino_2:dict, rino_3:dict, screen:pygame.Surface, player:dict, game:dict)-> None:
    """Checks the condition for the artifact to appear and handles its collection.

    Args:
    trunk (dict): The first trunk object.
    trunk_2 (dict): The second trunk object.
    rino (dict): The first rino object.
    rino_2 (dict): The second rino object.
    rino_3 (dict): The third rino object.
    screen (pygame.Surface): The game screen.
    player (dict): The player object.
    game (dict): The game object.
    """
    if not trunk["live"] and not trunk_2["live"] and not rino["live"] and not rino_2["live"] and not rino_3["live"]:
        screen.blit(artifact_image, (ARTIFACT_POSITION[0], ARTIFACT_POSITION[1]))
        if not player["got_artifact"]:
            if detect_collition(player["hitbox"]["rct"], player["artifact_rect"]):
                player["got_artifact"] = True
                game["show_popup"] = True
                game["popup_start_time"] = pygame.time.get_ticks()

def show_hud(screen:pygame.Surface, player:dict, font:pygame.font)-> None:
    """Displays the Heads-Up Display (HUD) on the screen.

    Args:
    screen (pygame.Surface): The game screen.
    player (dict): The player object.
    font (pygame.font): The font to use for text in the HUD.
    """

    get_health_image(player)
    screen.blit(player["heart_image"], (HEARTS_GUI_POSITION[0], HEARTS_GUI_POSITION[1]))
    screen.blit(stars_hud, (STARS_POSITION[0], STARS_POSITION[1]))
    show_text(screen, (STARS_POSITION[0] + 80, STARS_POSITION[1] + 25), f"{player["stars_count"]}", font, YELLOW)

def endscreen(game:dict, player:dict, screen:pygame.Surface, font:pygame.font)-> None:
    """Handles the end screen logic and display.

    Args:
    game (dict): The game object.
    player (dict): The player object.
    screen (pygame.Surface): The game screen.
    font (pygame.font): The game font.
    """
    if game["show_popup"]:
        current_time = pygame.time.get_ticks()
        if current_time - game["popup_start_time"] >= POPUP_DURATION:
            game["show_popup"] = False
            player["name"] = get_player_name(screen, font)
            save_score(player)
            quit_game()
        else:
            screen.blit(gameover_popup, (0,0))
            game["in_pause"] = True

    if player["got_artifact"]:
        game["show_popup"] = True

def score_calculator(player:dict)-> int:
    """Calculates the player's score based on their hearts and stars collected.

    Args:
    player (dict): The player object.

    Returns:
    int: The calculated final score.
    """
    match player["hearts"]:
        case 5:
            score = player["stars_count"] * 16
        case 4:
            score = player["stars_count"] * 15
        case 3:
            score = player["stars_count"] * 14
        case 2:
            score = player["stars_count"] * 13
        case 1:
            score = player["stars_count"] * 12
        case 0:
            score = player["stars_count"] * 11
    return score

def save_score(player:dict)-> None:
    """
    Saves the player's name and score to a CSV file.

    Args:
    player (dict): The player object.
    """
    with open('./src/scores.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([player["name"], player["score"]])

def get_player_name(screen:pygame.Surface, font:pygame.font):
    """ Creates a text box in the center of the screen where the user can type
    their name.

    Args:
        screen (pygame.Surface): The game screen
        font (pygame.font): The font used to render the text on the screen.

    Returns:
        str: The name entered by the user.
    """
    # Box where player will write his name
    input_box = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 25, 200, 50)
    # Box color
    color = GREEN
    # Inicialize the text as an empty string
    text = ''
    # Text imput not done
    done = False

    while not done:
        # Detect pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                # player press enter when finishes writting his name
                if event.key == pygame.K_RETURN:
                    done = True
                # Player can delete text
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                # Every other key will be saved on text
                else:
                    text += event.unicode
        # Set a background
        screen.blit(menu_background, (0, 0))
        # Rendering the text
        txt_surface = font.render(text, True, color)
        # Make the input box big enough to fit the text
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        # Drawing the text, a title and the box
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)
        show_text(screen, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50), "Enter your name:", font, (255, 255, 255))
        pygame.display.flip()
    return text