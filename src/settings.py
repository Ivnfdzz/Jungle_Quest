def resize_with_aspect_ratio(size:list, scale_factor:float)-> list:
    """Resizes a given size while maintaining its aspect ratio.

    Args:
    size (list): A tuple or list containing the original width and height.
    scale_factor (float): The factor by which to scale the size.

    Returns: 
    list: A list containing the new width and height, scaled according to the given factor.
    """
    width, height = size
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)
    return [new_width, new_height]

# SCREEN
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
MID_SCREEN_WIDTH = SCREEN_WIDTH // 2
MID_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
SCREEN_CENTER = (MID_SCREEN_WIDTH, MID_SCREEN_HEIGHT)
MUTE_TEXT_POS = (80, SCREEN_HEIGHT - 30)
FPS = 60

# Buttons size
SCALE_FACTOR = 3.5

PLAY_BUTTON_SIZE = resize_with_aspect_ratio((56, 24), SCALE_FACTOR)
BACK_BUTTON_SIZE = resize_with_aspect_ratio((56, 56), 1)
LEADERBOARD_BUTTON_SIZE = resize_with_aspect_ratio((120, 24), SCALE_FACTOR)
MAIN_MENU_BUTTON_SIZE = resize_with_aspect_ratio((88, 24), SCALE_FACTOR)
MUTE_BUTTON_SIZE = resize_with_aspect_ratio((56, 24), SCALE_FACTOR)
OPTIONS_BUTTON_SIZE = resize_with_aspect_ratio((72, 24), SCALE_FACTOR)
QUIT_BUTTON_SIZE = resize_with_aspect_ratio((56, 24), SCALE_FACTOR)

# Buttons position
START_BUTTON_POSITION = [MID_SCREEN_WIDTH, 250]
BACK_BUTTON_POSITION = [5, 5]
LEADERBOARD_BUTTON_POSITION = [MID_SCREEN_WIDTH, 300]
MAIN_MENU_BUTTON_POSITION = [MID_SCREEN_WIDTH, 500]
MUTE_BUTTON_POSITION = []
OPTIONS_BUTTON_POSITION = [MID_SCREEN_WIDTH, 400]
QUIT_BUTTON_POSITION = MAIN_MENU_BUTTON_POSITION

# Colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)

# Player
PJ_WIDTH = 70
PJ_HEIGHT = 90
PJ_SPEED = 4
PJ_SIZE = [PJ_WIDTH, PJ_HEIGHT]
PJ_POSITION = [50, 430]
GRAVITY = 1
JUMP_STRENGTH = 20
JUMP_2_STRENGTH = 15
GROUND_LEVEL = 600
PLAYER_HIT_INVULNERABILITY_DURATION = 2000
LASER_WIDTH = 10
LASER_HEIGHT = 5
LASER_SPEED = 15

# Item
ITEM_FEEDBACK_WIDTH = 60
ITEM_FEEDBACK_HEIGHT = 60
VISUAL_EFFECT_DURATION = 300

# Trunk
TRUNK_WIDTH = 70
TRUNK_HEIGHT = 60
TRUNK_BULLET_SPEED = 10
TRUNK_SHOOT_TIME = 1200
TRUNK_POSITION = {"1": [675, 180],
"2": [675, 460],
"3": [95, 57],
"4": [653,130],
"5": [78,130],
"6": [700, 160],
"7": [50, 160],
}

TRUNK_POS_AND_VISION = {
"1": {"position": [675, 180], "vision": {"x": 0, "y": 170, "width": 800, "height": 80}},
"2": {"position": [675, 460], "vision": {"x": 0, "y": 445, "width": 800, "height": 80}},
"3": {"position": [95, 57], "vision": {"x": 0, "y": 15, "width": 800, "height": 120}},
"4": {"position": [653,130], "vision": {"x": 0, "y": 115, "width": 800, "height": 80}},
"5": {"position": [78,130], "vision": {"x": 0, "y": 115, "width": 800, "height": 80}},
"6": {"position": [700, 160], "vision": {"x": 0, "y": 100, "width": 800, "height": 80}},
"7": {"position": [50, 160], "vision": {"x": 0, "y": 100, "width": 800, "height": 80}}
}

# Rino
RINO_WIDTH = 90
RINO_HEIGHT = 60
RINO_SPEED = 10
RINO_POS_AND_LIMIT = {
"1": {"position":[675, 460], "limit": 0},
"2": {"position":[675, 310], "limit": 325},
"3": {"position":[700, 460], "limit": 0},
"4": {"position":[700, 310], "limit": 0},
"5": {"position":[100, 310], "limit": 0},
"6": {"position":[500, 460], "limit": 0},
"7": {"position":[700, 310], "limit": 0},
"8": {"position":[50, 310], "limit": 0},
"9": {"position":[500, 160], "limit": 0}
}

# Artifact
ARTIFACT_WIDTH = 32
ARTIFACT_HEIGHT = 32
ARTIFACT_SIZE = resize_with_aspect_ratio((ARTIFACT_WIDTH, ARTIFACT_HEIGHT), 3)
ARTIFACT_POSITION = [690, 130]

# Invulerability star
INVULNERABILITY_STAR_SIZE = resize_with_aspect_ratio((32, 32), 1.5)
INVULNERABILITY_STAR_POSITION = [20, 57]
INVULNERABILITY_STAR_DURATION = 2000
INVULNERABILITY_SHIELD_WIDTH = 100
INVULNERABILITY_SHIELD_HEIGHT = 100
INVULNERABILITY_SHIELD_SIZE = [INVULNERABILITY_SHIELD_WIDTH, INVULNERABILITY_SHIELD_HEIGHT]

# Hearts
HEARTS_GUI_SIZE = [230, 40]
HEARTS_GUI_POSITION = [SCREEN_WIDTH - HEARTS_GUI_SIZE[0], 3]

# Stars
STARS_SIZE = resize_with_aspect_ratio((32, 32), 1.5)
STARS_POSITION = [5, 5]

# Popup
POPUP_DURATION = 4000
POPUP_SIZE = SCREEN_SIZE