import pygame
import sys
from settings import *
from loads import *
from tools import *
from main import level_1


SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jungle Quest")
pygame.display.set_icon(pygame.image.load("./src/assets/images/gui/icon.png"))

pygame.init()
pygame.mixer.init()
font = pygame.font.SysFont("Daydream", 25)

music_playing = True

def toggle_music():
    global music_playing
    if music_playing:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
    music_playing = not music_playing

# Función para dibujar un botón con imagen centrado
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

def go_to_game():
    start_button_sound.play()
    level_1()

def go_to_leaderboards():
    press_button_sound.play()
    leaderboards_screen()

def go_to_options():
    press_button_sound.play()
    options_screen()

def quit_game():
    pygame.quit()
    sys.exit()

# Pantalla principal
def main_menu():
    while True:
        SCREEN.blit(main_menu_background, (0,0))
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

# Otras pantallas
def play_scenario():
    while True:
        SCREEN.blit(menu_background, (0,0))
        mouse_over_button = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
        text_surf = font.render("SCREEN 1", True, BLACK)
        SCREEN.blit(text_surf, (SCREEN_WIDTH // 2 - text_surf.get_width() // 2, SCREEN_HEIGHT // 2 - text_surf.get_height() // 2))
        if draw_image_button(back_button, (MID_SCREEN_WIDTH, 500), main_menu):
            mouse_over_button = True
        if mouse_over_button:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.flip()

def leaderboards_screen():
    while True:
        SCREEN.blit(menu_background, (0,0))
        mouse_over_button = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
        text_surf = font.render("SCREEN 2", True, BLACK)
        SCREEN.blit(text_surf, (SCREEN_WIDTH // 2 - text_surf.get_width() // 2, SCREEN_HEIGHT // 2 - text_surf.get_height() // 2))
        if draw_image_button(back_button, (50, 50), main_menu):
            mouse_over_button = True
        if mouse_over_button:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        pygame.display.flip()

def options_screen():
    global music_playing
    while True:
        SCREEN.blit(menu_background, (0, 0))
        mouse_over_button = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
        text_surf = font.render("Options", True, GREEN)
        SCREEN.blit(text_surf, (SCREEN_WIDTH // 2 - text_surf.get_width() // 2, 150 - text_surf.get_height() // 2 - 100))
        # Botón de volver al menú principal
        if draw_image_button(back_button, (50, 50), main_menu):
            mouse_over_button = True
        # Botón de mute/unmute música
        if draw_image_button(mute_button, (MID_SCREEN_WIDTH, MID_SCREEN_HEIGHT), toggle_music):
            mouse_over_button = True
        if mouse_over_button:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        pygame.display.flip()


def gameover_screen():
    while True:
        SCREEN.blit(menu_background, (0,0))
        mouse_over_button = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
        text_surf = font.render("SCREEN 2", True, BLACK)
        SCREEN.blit(text_surf, (SCREEN_WIDTH // 2 - text_surf.get_width() // 2, SCREEN_HEIGHT // 2 - text_surf.get_height() // 2))
        if draw_image_button(back_button, (50, 50), main_menu):
            mouse_over_button = True
        if mouse_over_button:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

main_menu()