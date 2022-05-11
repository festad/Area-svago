import os

import pygame
import pygame_menu
from pygame_menu.themes import Theme

WIN_WIDTH  = 800
WIN_HEIGHT = 600
WIN_SIZE   = (WIN_WIDTH,WIN_HEIGHT)

MENU_WIDTH  = 800
MENU_HEIGHT = 600
MENU_SIZE   = (MENU_WIDTH,MENU_HEIGHT)

MENU_TITLE = 'SPACE INVADERS'

BG_IMAGE_NAME = 'space_invaders_bg.png'

BG_IMAGE_PATH = os.path.join(os.path.dirname(__file__), BG_IMAGE_NAME)


def start_the_game():
    pass

def rules_of_the_game():
    pass

def explanation_video():
    pass


def personalization_of_theme():
    # You can start from an existing
    # theme if it looks somewhat like
    # the one you would like to get.
    mytheme = pygame_menu.themes.THEME_DARK.copy()

    # Create the colors you like,
    # you can use the tool at
    # https://www.w3schools.com/colors/colors_rgb.asp
    # to help yourself with the choice.
    
    BLUE_COLOR = (0,55,95)
    # mytheme.background_color = BLUE_COLOR

    # I think it's better to find some
    # image online and set it as a background
    if not os.path.isfile(BG_IMAGE_PATH):
        print('Background image not found!\n'\
        + 'Using a black background instead.')
        bg_image = (0,0,0)
    else:
        print(f'Background image at: {BG_IMAGE_PATH}')
        bg_image = pygame_menu.baseimage.BaseImage(
            image_path=BG_IMAGE_PATH,
            drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
        )
    mytheme.background_color = bg_image
    
    # New personalizations go here :
    mytheme.title_background_color = (0,0,0,0) # Transparent

    LIGHT_VIOLET_COLOR = (230,0,150)
    mytheme.widget_font_color = LIGHT_VIOLET_COLOR
    mytheme.title_font_color  = LIGHT_VIOLET_COLOR
    mytheme.title_offset = (int(MENU_WIDTH/2)-250,
                            int(MENU_HEIGHT/4))

    mytheme.title_font  = pygame_menu.font.FONT_8BIT
    mytheme.widget_font = pygame_menu.font.FONT_8BIT
    
    return mytheme

def initialize_menu():
    mytheme = personalization_of_theme()
    
    menu = pygame_menu.Menu(width=MENU_WIDTH,
                            height=MENU_HEIGHT,
                            theme=mytheme,
                            title=MENU_TITLE)
    addName = menu.add.text_input('Name: ', default='')
    
    menu.add.button('Play', start_the_game)
    menu.add.button('Rules', rules_of_the_game)
    menu.add.button('Video', explanation_video)
    menu.add.button('Quit', pygame_menu.events.EXIT)

    return menu
    

def main():
    pygame.init()
    surface = pygame.display.set_mode(WIN_SIZE)
    menu = initialize_menu()
    menu.mainloop(surface)

if __name__ == '__main__':
    main()
