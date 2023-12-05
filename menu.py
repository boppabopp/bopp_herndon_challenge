import pygame

class Menu:
    def __init__(self, screen):
        # Initialize the Menu object with the given Pygame surface (screen)
        self.screen = screen

        # Define fonts for regular text and title
        self.font = pygame.font.Font('fonts/From Cartoon Blocks.ttf', 40)  # Set font for all of this
        self.title_font = pygame.font.Font('fonts/From Cartoon Blocks.ttf', 60)  # Same font but larger

        # Define dimensions for the start button
        button_width = 200
        button_height = 100

        # Create a rectangle representing the start button
        self.start_button = pygame.Rect((screen.get_width() - button_width) // 2,
                                        screen.get_height() // 2 - 100,
                                        button_width, button_height)

    def display_menu(self):
        # Set background color to white
        self.screen.fill((255, 255, 255))

        # Display title
        title_text = self.title_font.render("Herndon Challenge", True, (0, 0, 0))  # Black text
        title_rect = title_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 4))
        self.screen.blit(title_text, title_rect)

        # Display directions
        directions = [
            "Player 1: Use the arrow keys to jump and move.",
            "Player 2: Use the W, A, D keys to jump and move.",
            "Each time a player reaches the cover, they earn one point.",
            "The player with the most points after 60 seconds wins!"
        ]

        y_position = self.screen.get_height() // 2 + 80
        for direction in directions:  # puts the directions on the screen one line at a time
            direction_text = self.font.render(direction, True, (0, 0, 0))  # Black text
            direction_rect = direction_text.get_rect(center=(self.screen.get_width() // 2, y_position))
            self.screen.blit(direction_text, direction_rect)
            y_position += 30

        # Draw enlarged start button
        start_text = self.font.render("Start Game", True, (255, 255, 255))  # White text
        start_rect = start_text.get_rect(center=self.start_button.center)
        pygame.draw.rect(self.screen, (56, 70, 110), self.start_button)  # Draw the button rectangle
        self.screen.blit(start_text, start_rect)

    def handle_input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Check for left mouse button click
            mouse_pos = event.pos
            if self.start_button.collidepoint(mouse_pos):
                return True  # Start button clicked
        return False
