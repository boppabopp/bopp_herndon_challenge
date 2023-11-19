import pygame
class Herndon(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.image = pygame.Surface((300, 600))
        self.image.fill((170, 170, 170))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (screen.get_width()/2 + 80, 660)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, screen):
        pass