import pygame


class Herndon(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()

        # Create the main tower surface
        self.image = pygame.Surface((300, 500), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.midbottom = (screen.get_width() // 2 + 80, 660)

    def draw_triangle(self):
        # Create the blue triangle surface
        triangle_width = 50
        triangle_height = 100
        triangle_color = (0, 0, 255)  # Blue color
        triangle = pygame.Surface((triangle_width, triangle_height), pygame.SRCALPHA)
        pygame.draw.polygon(triangle, triangle_color,
                            [(0, triangle_height), (triangle_width // 2, 0), (triangle_width, triangle_height)])

        # Calculate the position to draw the triangle above the top of the tower
        triangle_x = (self.image.get_width() - triangle_width) // 2
        triangle_y = self.rect.top - triangle_height

        # Blit the blue triangle onto the tower surface
        self.image.blit(triangle, (triangle_x, triangle_y))

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
