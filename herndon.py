import pygame


class Herndon(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()

        # Create the main tower surface
        self.image = pygame.Surface((300, 500), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.midbottom = (screen.get_width() // 2 + 80, 660)

    def draw(self, screen):
        # Create a temporary surface to hold the tower and triangle
        temp_surface = pygame.Surface((300, 500), pygame.SRCALPHA)

        # Draw the tower
        pygame.draw.rect(temp_surface, (170, 170, 170), (0, 0, 300, 500))

        # Draw the triangle on the temporary surface
        self.draw_triangle()

        # Draw the temporary surface onto the screen
        screen.blit(temp_surface, self.rect.topleft)
    def update(self, screen):
        pass
