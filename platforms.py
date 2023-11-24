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
    def update(self, screen, herndon, plebe):
        if self.rect.right > herndon.rect.right:
            self.rect.right -= 1.0
        if self.rect.left < herndon.rect.left:
            self.rect.left += 1.0

