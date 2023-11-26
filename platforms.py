import pygame
from random import randint

class Platform(pygame.sprite.Sprite):
    def __init__(self, screen, y):
        super().__init__()

        # Create a surface for the platform
        self.image = pygame.Surface((60, 20))
        self.image.fill((150, 150, 150))
        self.rect = self.image.get_rect()

        # Get the width of the screen
        screen_width = screen.get_width()

        # Define the range of x-coordinates for the platform based on Herndon's position
        range_of_herndon_x = (screen_width / 2 + 80 - 150, screen_width / 2 + 80 + 150)

        # Set a random x-coordinate within the specified range
        random_x = randint(int(range_of_herndon_x[0]), int(range_of_herndon_x[1]))

        # Set the position of the platform as a vector
        self.rect.midbottom = (random_x, y)

        # Set initial movement direction
        self.direction = 1  # 1 for right, -1 for left
        self.speed = 0.1  # Adjust the speed as needed

        # Counter to control movement updates
        self.counter = 0

    def update(self, screen, herndon, plebe):
        # Increment the counter
        self.counter += 1

        # Check if the counter reaches a threshold for movement
        if self.counter >= 1 / self.speed:
            # Check if the platform is within the bounds of Herndon before moving
            if (herndon.rect.left < self.rect.left and self.direction == -1) or \
               (herndon.rect.right > self.rect.right and self.direction == 1):
                self.rect.x += self.direction

            # Reverse direction if the platform reaches the screen's edge
            if self.rect.right >= herndon.rect.right or self.rect.left <= herndon.rect.left:
                self.direction = -self.direction  # Reverse direction

            # Reset the counter
            self.counter = 0
