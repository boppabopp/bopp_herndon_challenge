import pygame
from herndon import *
from pygame import mixer

class Plebe(pygame.sprite.Sprite):

    def __init__(self, screen):
        super().__init__()

        # Load the Plebe image and scale it
        self.image = pygame.image.load('images\plebe.png')
        self.image = pygame.transform.scale(self.image, (50, 100))

        # Set the initial position of the Plebe
        self.rect = self.image.get_rect()
        self.rect.x = screen.get_width() / 2
        self.rect.y = screen.get_height() - self.rect.height

        # Set initial velocities and jumping status
        self.velocity_x = 0
        self.velocity_y = 0
        self.jumping = False
        jump_sound = mixer.Sound('audio/jump.wav')

    def update(self, screen, platforms, herndon):
        # Apply gravity to the Plebe's vertical velocity
        self.velocity_y += .2

        # Update the position based on velocities
        self.rect.x += self.velocity_x / 11
        self.rect.y += self.velocity_y / 11

        # Check if the Plebe is on the ground
        if self.rect.y >= screen.get_height() - self.rect.height:
            self.rect.y = screen.get_height() - self.rect.height
            self.velocity_y = 0
            self.jumping = False

        # Check for collision with platforms
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                # If the Plebe is on top of a platform, stop falling
                if self.rect.bottom - 4 <= platform.rect.top:
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
            self.velocity_y = -21
            mixer.Sound.play(jump_sound)

    def draw(self, screen):
        # Draw the Plebe on the screen
        screen.blit(self.image, self.rect)

