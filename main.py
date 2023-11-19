import pygame
from plebe1 import *
from helpers import *
from herndon import *
from platforms import *
from random import randint

pygame.init()

# make the clock
clock = pygame.time.Clock()

# set resolution of the game window
WIDTH = 1080
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# make the background (only once)
background = make_background(screen)

# create the Plebe sprite
plebe1 = Plebe(screen)
plebe_group = pygame.sprite.Group()
plebe_group.add(plebe1)

# create the Herndon sprite
herndon1 = Herndon(screen)
herndon_group = pygame.sprite.Group()
herndon_group.add(herndon1)

# create platforms
platform_group = pygame.sprite.Group()
range_of_herndon_y_1 = (640, 660)
for j in range(5):
    random_y = randint(range_of_herndon_y_1[0], range_of_herndon_y_1[1])
    random_y -= j * 100
    platform = Platform(screen, random_y)
    platform_group.add(platform)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                plebe1.velocity_x += 6
            if event.key == pygame.K_LEFT:
                plebe1.velocity_x -= 6
            if event.key == pygame.K_UP:
                plebe1.jump()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                plebe1.velocity_x -= 6
            if event.key == pygame.K_LEFT:
                plebe1.velocity_x += 6

        if (
            herndon1.rect.midtop[1] + 20 <= plebe1.rect.bottom <= herndon1.rect.midtop[1] - 20
            and (herndon1.rect.centerx - 20 <= plebe1.rect.centerx <= herndon1.rect.centerx + 20)
        ):
            # You can add game over logic here
            print("Game Over!")
            running = False


    # Put background on the screen
    screen.blit(background, (0, 0))

    # Draw entities
    herndon_group.draw(screen)
    herndon1.draw(screen)
    herndon1.update(screen)

    platform_group.draw(screen)

    plebe_group.draw(screen)

    # Update entities
    plebe_group.update(screen, platform_group)
    herndon_group.update(screen)
    platform_group.update(screen)
    # flip the display so that we can see what we did
    pygame.display.flip()

pygame.quit()