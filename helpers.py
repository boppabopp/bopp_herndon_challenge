# helpers file
import pygame


def make_background(screen):
    w = screen.get_width()
    h = screen.get_height()

    # Load the original background image, smooth scale to width and height of scree
    original_background = pygame.image.load('images/ckground.jpg').convert_alpha()
    original_background = pygame.transform.smoothscale(original_background, (w, h))

    return original_background
