import pygame


class Herndon(pygame.sprite.Sprite):

    # initialize class and inherit from sprite class
    def __init__(self, screen):
        super().__init__()

        # Set the width and height of the tower
        self.width = 300
        self.height = 500

        # Set the position of the tower
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.midbottom = (screen.get_width() // 2 + 80, screen.get_height())

        # Draw the tower on the surface
        pygame.draw.rect(self.image, (170, 170, 170), (0, 0, self.width, self.height))

    def draw(self, screen):
        # Draw the tower on the screen
        screen.blit(self.image, self.rect.topleft)

    def update(self):
        pass