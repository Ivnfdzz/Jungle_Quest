import pygame
import sys
import json
import os
from settings import *
from loads import *
from tools import *
from levels import level_1

# Paths to configuration and scores files
config_path = os.path.join("src", "config.json")
csv_path = os.path.join("src", "scores.csv")

# Function to load the configuration from a JSON file
def load_config():
    # Cheks if config file exists
    if os.path.exists(config_path):
        # Read the json file
        with open(config_path, "r") as file:
            return json.load(file)
    else:
        # Default config
        return {"music_playing": True}

# Function to save the configuration to a JSON file
def save_config(config):
    with open(config_path, "w") as file:
        json.dump(config, file, indent=4)

# load scores from a CSV file and sort them
def load_scores():
    # Return list
    scores = []
    # Check if the csv file exists
    if os.path.exists(csv_path):
        # Open csv file on read mode
        with open(csv_path, newline='') as csvfile:
            # Saves the content in the csv
            reader = csv.reader(csvfile)
            for row in reader:
                # Check if exists at least a score
                if len(row) >= 2:
                    try:
                        # Saves the score as a tuple
                        scores.append((row[0], int(row[1])))
                    except ValueError:
                        # If row 2 is not a number prints an error
                        print(f"Error converting score to int for row: {row}")
                else:
                    # If there is not enough elements in the row
                    print(f"Row has insufficient elements: {row}")
    # Based on the second tuple's element (score), sorts the list 
    scores.sort(key=lambda x: x[1], reverse=True)
    # Return the best 10 scores
    return scores[:10]


def display_scores(scores):
    # Y position    
    y_offset = 200 
    for i, (name, score) in enumerate(scores):
        text = f"{i+1}. {name}: {score}"
        text_surf = font.render(text, True, GREEN)
        SCREEN.blit(text_surf, (SCREEN_WIDTH // 2 - text_surf.get_width() // 2, y_offset))
        y_offset += 30

# Initialize the main screen and other Pygame settings
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jungle Quest")
pygame.display.set_icon(pygame.image.load("./src/assets/images/gui/icon.png"))

pygame.init()
pygame.mixer.init()
font = pygame.font.SysFont("Daydream", 25)

# Load the configuration and set the music playing state
config = load_config()
music_playing = config.get("music_playing", True)

if music_playing:
    pygame.mixer.music.play(-1)
else:
    pygame.mixer.music.pause()

# Function to toggle the music playing state
def toggle_music():
    global music_playing
    music_playing = not music_playing
    if music_playing:
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.pause()
    config["music_playing"] = music_playing
    save_config(config)

# Function to draw a button with an image and handle its click action
def draw_image_button(image, center_pos, action=None):
    rect = image.get_rect(center=center_pos)
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    hovered = rect.collidepoint(mouse_pos)
    SCREEN.blit(image, rect.topleft)
    if hovered and click[0] == 1 and action:
        pygame.time.delay(200)
        action()
    return hovered

# Function to start the game
def go_to_game():
    start_button_sound.play()
    level_1()

# Function to display the leaderboards screen
def go_to_leaderboards():
    press_button_sound.play()
    leaderboards_screen()

# Function to display the options screen
def go_to_options():
    press_button_sound.play()
    options_screen()

# Function to quit the game
def quit_game():
    pygame.quit()
    sys.exit()

# Main menu function to display the main menu and handle navigation
def main_menu():
    while True:
        SCREEN.blit(main_menu_background, (0, 0))
        mouse_over_button = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        if draw_image_button(play_button, (MID_SCREEN_WIDTH, 220), go_to_game):
            mouse_over_button = True
        if draw_image_button(leaderboard_button, (MID_SCREEN_WIDTH, 330), go_to_leaderboards):
            mouse_over_button = True
        if draw_image_button(options_button, (MID_SCREEN_WIDTH, 440), go_to_options):
            mouse_over_button = True
        if draw_image_button(quit_button, (MID_SCREEN_WIDTH, 550), quit_game):
            mouse_over_button = True

        if mouse_over_button:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        pygame.display.flip()

# Display the leaderboards screen
def leaderboards_screen():
    scores = load_scores()
    while True:
        SCREEN.blit(menu_background, (0, 0))
        mouse_over_button = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
        
        text_surf = font.render("Leaderboards", True, GREEN)
        SCREEN.blit(text_surf, (SCREEN_WIDTH // 2 - text_surf.get_width() // 2, 50))
        
        display_scores(scores)
        
        if draw_image_button(back_button, (50, 50), main_menu):
            mouse_over_button = True
        if mouse_over_button:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        
        pygame.display.flip()

# Display the options screen
def options_screen():
    global music_playing
    # Game loop
    while True:
        SCREEN.blit(menu_background, (0, 0))
        mouse_over_button = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
        # Title
        text_surf = font.render("Options", True, GREEN)
        SCREEN.blit(text_surf, (SCREEN_WIDTH // 2 - text_surf.get_width() // 2, 150 - text_surf.get_height() // 2 - 100))
        # Back button
        if draw_image_button(back_button, (50, 50), main_menu):
            mouse_over_button = True

        # Mute button
        if draw_image_button(mute_button, (MID_SCREEN_WIDTH, MID_SCREEN_HEIGHT), toggle_music):
            mouse_over_button = True
        # Change cursor
        if mouse_over_button:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        pygame.display.flip()

main_menu()
