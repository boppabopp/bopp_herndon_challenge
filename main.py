# setting up pygame
import pygame
from plebe1 import *
from helpers import *
from herndon import *
pygame.init()
# make the clock
clock = pygame.time.Clock()
# set resolution of game window
WIDTH = 1080
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# make the background (only once)
background = make_background(screen)

plebe1 = Plebe(screen)
plebe_group = pygame.sprite.Group()
plebe_group.add(plebe1)

herndon1 = Herndon(screen)
herndon_group = pygame.sprite.Group()

clock = pygame.time.Clock()
clock.tick(60)

running = True
while running:
    # get events
    for event in pygame.event.get():
        # if we quit, the game closes
        if event.type == pygame.QUIT:
            running = False

        # if we press the left or right arrow keys, the plebe moves left or right one space
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                plebe1.velocity_x += 5
            if event.key == pygame.K_LEFT:
                plebe1.velocity_x -= 5
            if event.key == pygame.K_SPACE:
                plebe1.jump()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                plebe1.velocity_x -= 5
            if event.key == pygame.K_LEFT:
                plebe1.velocity_x += 5

    # put background on the screen
    screen.blit(background, (0, 0))


    # put the plebes on the screen
    herndon_group.draw(screen)
    plebe_group.draw(screen)


     # continuously update the groups
    plebe_group.update(screen)
    herndon_group.update()


    # flip the display so that we can see what we did
    pygame.display.flip()

pygame.quit()
