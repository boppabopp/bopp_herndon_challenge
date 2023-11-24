import pygame
from random import randint

# This function will take two surfaces and center the second surface on the first one
def center_surfaces(bg, fg):
    # Get the background width and height
    bg_width = bg.get_width()
    bg_height = bg.get_height()
    # Get the foreground surface width and height
    fg_width = fg.get_width()
    fg_height = fg.get_height()
    # Blit the foreground surface on the background surface at the center
    bg.blit(fg, (bg_width // 2 - fg_width // 2, bg_height // 2 - fg_height // 2))

import pygame

def make_background(screen):
    w = screen.get_width()
    h = screen.get_height()

    # Load the original background image
    original_background = pygame.image.load('images/ckground.jpg')
    original_background = pygame.transform.scale(original_background, (w, h))

    return original_background

