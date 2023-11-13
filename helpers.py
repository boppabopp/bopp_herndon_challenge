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
    puffer_tile = pygame.image.load('assets/images/puffer_fish.png')
    water_tile = pygame.image.load('assets/images/fishTile_089.png')
    sand_top_tile = pygame.image.load('assets/images/fishTile_021.png')
    sand_tile = pygame.image.load('assets/images/fishTile_126.png')
    plant_tile = pygame.image.load('assets/images/fishTile_032.png')
    # get tile size info
    tile_width = water_tile.get_width()
    tile_height = water_tile.get_height()
    # make a background
    background = pygame.Surface((WIDTH,HEIGHT))
    # draw water tiles
    for x in range(0,WIDTH,tile_width):
        for y in range(0,HEIGHT,tile_height):
            background.blit(water_tile, (x,y))
    # draw sand tile
    for x in range(0,WIDTH,tile_width):
        background.blit(sand_tile, (x,HEIGHT-tile_height))
    # draw sand top tile
    for x in range(0,WIDTH,tile_width):
        background.blit(sand_top_tile, (x,HEIGHT-2*tile_height))
    # draw some plants!
    num_plants = 6
    for p in range(num_plants):
        background.blit(plant_tile,
                        (randint(0, WIDTH),randint(HEIGHT-3*tile_height, HEIGHT-1*tile_height)))
    return background