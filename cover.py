import pygame
class Cover(pygame.sprite.Sprite):
    def __init__(self, screen, herndon, radius):
        super().__init__()

        # Set the height of the tower to the full height of the screen
        self.image = pygame.image.load('images\cover.png').convert_alpha()  # convert alpha ensures transparency
        self.image = pygame.transform.smoothscale(self.image, (100, 200))
        self.rect = self.image.get_rect()

        # Set the position of the tower's bottom center
        self.rect.midbottom = (screen.get_width() // 2 + 80, herndon.rect.top)

        self.radius = radius
    def draw(self, screen):
        # Draw the tower on the screen
        screen.blit(self.image, self.rect)

    def update(self):
        # Update logic for Herndon can be added here if needed
        pass