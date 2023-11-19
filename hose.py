import pygame
class Hose(pygame.sprite.Sprite):

    def __init__(self, screen):
        super().__init__()
        self.image = pygame.image.load('images\hose.jpg')
        self.rect = self.image.get_rect()
        # self.rect.x = screen.get_width()/2
        # self.rect.y = screen.get_height()/2
        self.rect.bottomleft = 0, 700
        self.speed_y = 0

    def update(self, screen):
        self.rect.bottomleft = self.rect.bottomleft
        # self.rect.x = self.rect.x
        # self.rect.y = self.rect.y

    def draw(self, screen):
        screen.blit(self.image, self.rect)


