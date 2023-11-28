import pygame
from herndon import *
from pygame import mixer
import math

class Plebe(pygame.sprite.Sprite):

    def __init__(self, screen, image, radius, score):
        super().__init__()

        # Load the Plebe image and scale it
        self.image = image
        self.image = pygame.transform.smoothscale(image, (50, 100))

        # Set the initial position of the Plebe
        self.rect = self.image.get_rect()
        self.rect.x = screen.get_width() / 2
        self.rect.y = screen.get_height() - self.rect.height

        # Set initial velocities and jumping status
        self.velocity_x = 0
        self.velocity_y = 0
        self.jumping = False
        jump_sound = mixer.Sound('audio/jump.wav')

        self.radius = radius
        self.score = score

    def update(self, screen, platforms, herndon):
        # Apply gravity to the Plebe's vertical velocity
        self.velocity_y += 1

        # Update the position based on velocities
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

        # Check if the Plebe is on the ground
        if self.rect.y >= screen.get_height() - self.rect.height:
            self.rect.y = screen.get_height() - self.rect.height
            self.velocity_y = 0
            self.jumping = False

        platform_collisions_y = pygame.sprite.spritecollide(self, platforms, False)
        for platform in platform_collisions_y:
            if self.velocity_y > 0 and self.rect.bottom - 8 <= platform.rect.top:
                self.velocity_y = 0
                self.rect.y = platform.rect.y - self.rect.height
                self.jumping = False

        if self.rect.right >= screen.get_width():
            self.rect.x -= 1
        if self.rect.left <= 0:
            self.rect.x += 1

    def jump(self, jump_sound):
        # Perform a jump if not already jumping
        if not self.jumping:
            self.jumping = True
            self.velocity_y = -18
            mixer.Sound.play(jump_sound)

    def check_collision(self, cover):
        # Calculate the distance between the centers of the two sprites
        distance = math.sqrt(
            (self.rect.centerx - cover.rect.centerx) ** 2 + (self.rect.centery - cover.rect.centery) ** 2)

        # Check if the distance is less than the sum of the radii
        if distance < self.radius + cover.radius:
            return True  # Collision occurred
        else:
            return False  # No collision

    def draw(self, screen):
        # Draw the Plebe on the screen
        screen.blit(self.image, self.rect)
