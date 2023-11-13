# setting up pygame
import pygame
from helpers import *
pygame.init()
# make the clock
clock = pygame.time.Clock()
# set resolution of game window
WIDTH = 1080
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# make the background (only once)
background = make_background(screen)
