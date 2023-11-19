import pygame
from random import randint

# this function will take 2 surface and center the 2nd surface on the first one
def center_surfaces(bg, fg):
    # get the bg width and height
    bg_width = bg.get_width()
    bg_height = bg.get_height()
    # get the front surface width and height
    fg_width = fg.get_width()
    fg_height = fg.get_height()
    # blit the text on the surface
    bg.blit(fg, (bg_width/2 - fg_width/2, bg_height/2-fg_height/2 ))

def make_background(screen):
    WIDTH = screen.get_width()
    HEIGHT = screen.get_height()
    background = pygame.image.load('images\ckground.jpg').convert()
    background = pygame.transform.scale(background, (1080, 720))

    return background
