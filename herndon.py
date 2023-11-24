import pygame
import sys


class Herndon(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()

        # Set the height of the tower to the full height of the screen
        self.width = 300
        self.height = 500
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = self.image.get_rect()

        # Set the position of the tower's bottom center
        self.rect.midbottom = (screen.get_width() // 2 + 80, screen.get_height())

        # Draw the tower on the surface
        pygame.draw.rect(self.image, (170, 170, 170), (0, 0, self.width, self.height))

    def draw(self, screen):
        # Draw the tower on the screen
        screen.blit(self.image, self.rect.topleft)

    def update(self):
        # Update logic for Herndon can be added here if needed
        pass