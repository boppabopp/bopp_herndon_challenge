import pygame
from plebe1 import Plebe
from helpers import make_background
from herndon import Herndon
from platforms import Platform
from cover import Cover
from random import randint

pygame.init()

# Set resolution of the game window
WIDTH = 1080
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Make the clock
clock = pygame.time.Clock()

# Make the background (only once)
background = make_background(screen)

# Create the Plebe sprite
plebe1 = Plebe(screen)
plebe_group = pygame.sprite.Group()
plebe_group.add(plebe1)

# Create the Herndon sprite
herndon1 = Herndon(screen)
herndon_group = pygame.sprite.Group()
herndon_group.add(herndon1)

cover1 = Cover(screen, herndon1)
cover_group = pygame.sprite.Group()
cover_group.add(cover1)

# Create platforms
platform_group = pygame.sprite.Group()

# Define the range of y-coordinates for platforms based on Herndon's position
range_of_herndon_y = (herndon1.rect.top, herndon1.rect.bottom)

# Create platforms dynamically
for j in range(1, 8):
    random_y_i = ((herndon1.rect.bottom - herndon1.rect.top) / 8)
    random_y = herndon1.rect.bottom - random_y_i * j
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


        # Check for collision with Herndon
        if (
            pygame.Rect.colliderect(cover1.rect, plebe1)
        ):
            print("Game Over!")
            running = False

    # Update the position of Plebe and other game elements based on Plebe's movement
    plebe_group.update(screen, platform_group, herndon1)
    herndon_group.update()
    herndon1.update()
    cover_group.update()
    platform_group.update(screen, herndon1, plebe1)

    # Put background on the screen
    screen.blit(background, (0, 0))

    # Draw entities
    herndon_group.draw(screen)
    herndon1.draw(screen)


    # Draw a triangular obstacle above Herndon
    pygame.draw.polygon(
        screen,
        (150, 150, 150),
       [
           (herndon1.rect.midtop[0] - 150, herndon1.rect.top),
           (herndon1.rect.midtop[0], herndon1.rect.top - 100),
          (herndon1.rect.midtop[0] + 150, herndon1.rect.top),
       ],
    )

    platform_group.draw(screen)
    plebe_group.draw(screen)
    cover_group.draw(screen)

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
