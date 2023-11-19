import pygame
class Herndon(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.image = pygame.Surface((50, 150))
        self.image.fill((170, 170, 170))
        self.rect = self.image.get_rect()
        self.rect.x = screen.get_width()/2
        self.rect.y = 500

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, screen):
        pass