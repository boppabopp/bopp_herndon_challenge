import pygame
from herndon import *
from random import randint
class Platform(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.image = pygame.Surface((60, 20))
        self.image.fill((100, 50, 200))
        self.rect = self.image.get_rect()
        #self.rect.midbottom = (randint(0, 720), randint(0, 1080))
        self.rect.midbottom = (screen.get_width() / 2 + 80, 660)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, screen):
        pass