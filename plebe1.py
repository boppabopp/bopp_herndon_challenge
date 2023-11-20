import pygame
from herndon import *
class Plebe(pygame.sprite.Sprite):

    def __init__(self, screen):
        super().__init__()
        self.image = pygame.image.load('images\plebe.png')
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.rect = self.image.get_rect()
        self.rect.x = screen.get_width()/2
        self.rect.y = screen.get_height() - self.rect.height
        self.velocity_x = 0
        self.velocity_y = 0
        self.jumping = False

    def update(self, screen, platforms):
        self.velocity_y += 0.2
        self.rect.x += self.velocity_x/9
        self.rect.y += self.velocity_y/9

        if self.rect.y >= screen.get_height() - self.rect.height:
            self.rect.y = screen.get_height() - self.rect.height
            self.velocity_y = 0
            self.jumping = False

        for platform in platforms:
            if self.rect.colliderect(platform.rect):

                if self.rect.bottom - 4 <= platform.rect.top:
                    self.velocity_y = 0
                    self.rect.y = platform.rect.y - self.rect.height
                    self.jumping = False

    def jump(self):
        if not self.jumping:
            self.jumping = True
            self.velocity_y = -20

    def draw(self, screen):
        screen.blit(self.image, self.rect)
