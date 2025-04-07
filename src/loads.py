from settings import *
import pygame

def load_animation(path:str, ext:str, frames:int, width:int, height:int, starts_at_zero: bool = False)->tuple:
    """Loads and scales a series of images to create right and left facing animations.

    Args:
    path (str): The base path to the image files.
    ext (str): The file extension of the images.
    frames (int): The number of frames in the animation.
    width (int): The desired width of each frame.
    height (int): The desired height of each frame.
    starts_at_zero (bool, optional): If True, frame numbering starts at 0; otherwise, starts at 1. Defaults to False.

    Returns:
    tuple: A tuple containing two lists:
        - right_animation: List of images for the right-facing animation.
        - left_animation: List of images for the left-facing animation.

    Raises:
    FileNotFoundError: If an image file is not found, a warning is printed and the frame is skipped.
    """

    right_animation = []
    left_animation = []
    start_frame = 0 if starts_at_zero else 1
    for i in range(start_frame,frames):
        name = f"{path}{str(i)}.{ext}"
        try:
            image = pygame.transform.scale(pygame.image.load(name), (width, height))
        except FileNotFoundError:
            print(f"Warning: No file '{name}' found.")
            continue
        right_animation.append(image)
        left_animation.append(pygame.transform.flip(image, True, False))
    return (right_animation, left_animation)

def load_scaled_image(file_name:str, width:int, height:int)-> pygame.Surface:
    """Loads an image from a file and scales it to the specified dimensions.

    Args:
    file_name (str): The path to the image file.
    width (int): The desired width of the scaled image.
    height (int): The desired height of the scaled image.

    Returns:
    pygame.Surface: The loaded and scaled image.
    """
    image = pygame.image.load(file_name)
    image = pygame.transform.scale(image, (width, height))
    return image

pygame.mixer.init()

#images:
# Menu
main_menu_background = pygame.image.load("./src/assets/images/gui/menu_screens/main_menu_background.png")
menu_background = pygame.image.load("./src/assets/images/gui/menu_screens/menu_background.png")
gameover_background = pygame.image.load("./src/assets/images/gui/menu_screens/game_over.png")

# Buttons
back_button = load_scaled_image("./src/assets/images/gui/buttons/back_button.png", BACK_BUTTON_SIZE[0], BACK_BUTTON_SIZE[1])
leaderboard_button = load_scaled_image("./src/assets/images/gui/buttons/leaderboard_button.png", LEADERBOARD_BUTTON_SIZE[0], LEADERBOARD_BUTTON_SIZE[1])
main_menu_button = load_scaled_image("./src/assets/images/gui/buttons/main_menu_button.png", MAIN_MENU_BUTTON_SIZE[0], MAIN_MENU_BUTTON_SIZE[1])
mute_button = load_scaled_image("./src/assets/images/gui/buttons/mute_button.png", MUTE_BUTTON_SIZE[0], MUTE_BUTTON_SIZE[1])
options_button = load_scaled_image("./src/assets/images/gui/buttons/options_button.png", OPTIONS_BUTTON_SIZE[0], OPTIONS_BUTTON_SIZE[1])
play_button = load_scaled_image("./src/assets/images/gui/buttons/play_button.png", PLAY_BUTTON_SIZE[0], PLAY_BUTTON_SIZE[1])
quit_button = load_scaled_image("./src/assets/images/gui/buttons/quit_button.png", QUIT_BUTTON_SIZE[0],QUIT_BUTTON_SIZE[1])

# Music
pygame.mixer.music.load("./src/assets/sounds/music/music.wav")
pygame.mixer.music.set_volume(0.5)

#Backgrounds
level_1_background = load_scaled_image("./src/assets/images/enviorments/level_1.png", SCREEN_SIZE[0], SCREEN_SIZE[1])
level_2_background = load_scaled_image("./src/assets/images/enviorments/level_2.png", SCREEN_SIZE[0], SCREEN_SIZE[1])
level_3_background = load_scaled_image("./src/assets/images/enviorments/level_3.png", SCREEN_SIZE[0], SCREEN_SIZE[1])
level_4_background = load_scaled_image("./src/assets/images/enviorments/level_4.png", SCREEN_SIZE[0], SCREEN_SIZE[1])

# HUD:
# Hearts
hearts_5 = load_scaled_image("./src/assets/images/gui/hearts/hearts_5.png", HEARTS_GUI_SIZE[0], HEARTS_GUI_SIZE[1])
hearts_4 = load_scaled_image("./src/assets/images/gui/hearts/hearts_4.png", HEARTS_GUI_SIZE[0], HEARTS_GUI_SIZE[1])
hearts_3 = load_scaled_image("./src/assets/images/gui/hearts/hearts_3.png", HEARTS_GUI_SIZE[0], HEARTS_GUI_SIZE[1])
hearts_2 = load_scaled_image("./src/assets/images/gui/hearts/hearts_2.png", HEARTS_GUI_SIZE[0], HEARTS_GUI_SIZE[1])
hearts_1 = load_scaled_image("./src/assets/images/gui/hearts/hearts_1.png", HEARTS_GUI_SIZE[0], HEARTS_GUI_SIZE[1])
hearts_0 = load_scaled_image("./src/assets/images/gui/hearts/hearts_0.png", HEARTS_GUI_SIZE[0], HEARTS_GUI_SIZE[1])

# Stars_points
stars_hud = load_scaled_image("./src/assets/images/gui/stars.png", STARS_SIZE[0], STARS_SIZE[1])

# Popups
start_popup = load_scaled_image("./src/assets/images/gui/es_popups/es_start_popup.png", POPUP_SIZE[0], POPUP_SIZE[1])
popup_inv_star = load_scaled_image("./src/assets/images/gui/es_popups/es_inv_star_power_popup.png", POPUP_SIZE[0], POPUP_SIZE[1])
gameover_popup = load_scaled_image("./src/assets/images/gui/es_popups/es_gameover.png", POPUP_SIZE[0], POPUP_SIZE[1])
fail_gameover_popup = load_scaled_image("./src/assets/images/gui/es_popups/es_fail_gameover.png", POPUP_SIZE[0], POPUP_SIZE[1])

# Animations:
# Player
player_idle_right, player_idle_left  = load_animation("./src/assets/images/sprites/player/player_idle/player_idle_", "png", 6, PJ_WIDTH, PJ_HEIGHT)
player_run_right, player_run_left = load_animation("./src/assets/images/sprites/player/player_run/player_run_", "png", 6, PJ_WIDTH, PJ_HEIGHT)
player_jump_right, player_jump_left = load_animation("./src/assets/images/sprites/player/player_jump/player_jump_", "png", 2, PJ_WIDTH, PJ_HEIGHT)
player_shoot_right, player_shoot_left = load_animation("./src/assets/images/sprites/player/player_shoot/player_shoot_", "png", 3, PJ_WIDTH, PJ_HEIGHT)
player_running_shoot_right, player_running_shoot_left = load_animation("./src/assets/images/sprites/player/player_running_shoot/player_run_shoot_", "png", 6, PJ_WIDTH, PJ_HEIGHT)
player_special_shoot_right, player_special_shoot_left = load_animation("./src/assets/images/sprites/player/player_special_shoot/player_special_shoot_", "png", 3, PJ_WIDTH, PJ_HEIGHT)
player_special_running_shoot_right, player_special_running_shoot_left = load_animation("./src/assets/images/sprites/player/player_running_special_shoot/player_run_special_shoot_", "png", 6, PJ_WIDTH, PJ_HEIGHT)
player_bullet_right, player_bullet_left = load_animation("./src/assets/images/sprites/player/player_bullet/player_bullet_", "png", 4, PJ_WIDTH, PJ_HEIGHT // 2)

# Trunk
trunk_idle_right, trunk_idle_left = load_animation("./src/assets/images/sprites/trunk/idle/trunk_idle_", "png", 18, TRUNK_WIDTH, TRUNK_HEIGHT, True)
trunk_attack_right, trunk_attack_left = load_animation("./src/assets/images/sprites/trunk/attack/trunk_attack_", "png", 5, TRUNK_WIDTH, TRUNK_HEIGHT, True)

# Rino
rino_run_right, rino_run_left = load_animation("./src/assets/images/sprites/rino/run/Run_", "png", 6,RINO_WIDTH, RINO_HEIGHT, True)

# FX:
item_feedback, _ = load_animation("./src/assets/images/sprites/item-feedback/item-feedback-", "png", 4, ITEM_FEEDBACK_WIDTH, ITEM_FEEDBACK_HEIGHT)
inv_star_shield = load_scaled_image("./src/assets/images/sprites/invulnerability_star/star_shield.png", INVULNERABILITY_SHIELD_SIZE[0], INVULNERABILITY_SHIELD_SIZE[1])

# Items
invulnerability_star_animation, _ = load_animation("./src/assets/images/sprites/invulnerability_star/invulnerability_star_", "png", 4, INVULNERABILITY_STAR_SIZE[0], INVULNERABILITY_STAR_SIZE[1])
artifact_image = load_scaled_image("./src/assets/images/sprites/artifact.png", ARTIFACT_SIZE[0], ARTIFACT_SIZE[1])

# SFX

# Menu:
start_button_sound = pygame.mixer.Sound("./src/assets/sounds/fx/menu/Start.wav")
press_button_sound = pygame.mixer.Sound("./src/assets/sounds/fx/menu/UI_1.wav")

# Game:
enemy_killed_sound = pygame.mixer.Sound("./src/assets/sounds/fx/game/enemy_hit.wav")
inv_star_popup_sound = pygame.mixer.Sound("./src/assets/sounds/fx/game/inv_star_popup_sound.wav")
inv_star_use_sound = pygame.mixer.Sound("./src/assets/sounds/fx/game/inv_star_use_sound.wav")
player_hit_sound = pygame.mixer.Sound("./src/assets/sounds/fx/game/player_hit.wav")
player_jump_sound = pygame.mixer.Sound("./src/assets/sounds/fx/game/player_jump.wav")
player_laser_sound = pygame.mixer.Sound("./src/assets/sounds/fx/game/player_laser.wav")
trunk_shoot_sound = pygame.mixer.Sound("./src/assets/sounds/fx/game/trunk_shoot_sound.wav")
rino_hit_player_sound = pygame.mixer.Sound("./src/assets/sounds/fx/game/rino_hit_player.wav")