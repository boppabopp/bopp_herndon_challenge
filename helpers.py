# helpers.py
import pygame

def center_surfaces(bg, fg):
    bg_width = bg.get_width()
    bg_height = bg.get_height()
    fg_width = fg.get_width()
    fg_height = fg.get_height()
    bg.blit(fg, (bg_width // 2 - fg_width // 2, bg_height // 2 - fg_height // 2))

def make_background(screen):
    w = screen.get_width()
    h = screen.get_height()

    # Load the original background image
    original_background = pygame.image.load('images/ckground.jpg')
    original_background = pygame.transform.scale(original_background, (w, h))

    return original_background