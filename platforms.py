import pygame
from herndon import *
from random import randint
class Platform(pygame.sprite.Sprite):
    def __init__(self, screen, y):
        super().__init__()
        self.image = pygame.Surface((60, 20))
        self.image.fill((150, 150, 150))
        self.rect = self.image.get_rect()

        range_of_herndon_x = (screen.get_width()/2 + 80 - 150, screen.get_width()/2 + 80 + 150)
        random_x = randint(range_of_herndon_x[0], range_of_herndon_x[1])
        self.rect.midbottom = (random_x, y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, screen):
        pass