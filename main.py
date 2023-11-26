import pygame
from plebe1 import Plebe
from helpers import make_background
from herndon import Herndon
from platforms import Platform
from cover import Cover
from pygame.locals import *
from pygame import mixer

pygame.init()

# Set resolution of the game window
WIDTH = 1080
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Make the clock
clock = pygame.time.Clock()

# Make the background (only once)
background = make_background(screen)

# Create the Plebe sprites for Player 1 and Player 2
plebe1 = Plebe(screen)
plebe_group = pygame.sprite.Group()
plebe_group.add(plebe1)

plebe2 = Plebe(screen)
plebe_group.add(plebe2)

# Create the Herndon sprite
herndon1 = Herndon(screen)
herndon_group = pygame.sprite.Group()
herndon_group.add(herndon1)

# Create the Cover sprite
cover1 = Cover(screen, herndon1)
cover_group = pygame.sprite.Group()
cover_group.add(cover1)

# Create platforms
platform_group = pygame.sprite.Group()

# Define the range of y-coordinates for platforms based on Herndon's position
range_of_herndon_y = (herndon1.rect.top, herndon1.rect.bottom)

# Create platforms dynamically
for j in range(1, 6):
    random_y_i = ((herndon1.rect.bottom - herndon1.rect.top) / 6)
    random_y = herndon1.rect.bottom - random_y_i * j
    platform = Platform(screen, random_y)
    platform_group.add(platform)

# Initialize mixer and load audio files
mixer.init()
mixer.music.load('audio/music.oga')
mixer.music.play(-1)

jump_sound = mixer.Sound('audio/jump.wav')

# Set up fonts for timer and score
timer_font = pygame.font.Font('fonts/From Cartoon Blocks.ttf', 40)
score_font = pygame.font.Font('fonts/From Cartoon Blocks.ttf', 35)
winner_font = pygame.font.Font('fonts/From Cartoon Blocks.ttf', 80)

# Initialize timer and scores
timer_sec = 60
score1 = 0
score2 = 0

# Initialize the game start time, last collision time, and end time
start_time = pygame.time.get_ticks()
last_collision_time = 0
end_time = 0

# Cooldown duration in milliseconds (adjust as needed)
cooldown_duration = 1000  # 1000 milliseconds = 1 second

def show_timer():
    """Display the timer on the screen and set the game_over flag when the timer runs out."""
    global timer_sec, game_over

    current_time = pygame.time.get_ticks()
    elapsed_seconds = (current_time - start_time) // 1000

    if elapsed_seconds < timer_sec:
        timer_text = timer_font.render("00:%s" % str(timer_sec - elapsed_seconds), True, (0, 0, 0))
        screen.blit(timer_text, (50, 25))
    else:
        # Time is up, set the game_over flag
        game_over = True

def show_scores():
    """Display scores for Player 1 and Player 2 in the top right corner."""
    score1_text = score_font.render("Player 1 Score: %d" % score1, True, (0, 0, 0))
    score2_text = score_font.render("Player 2 Score: %d" % score2, True, (0, 0, 0))
    screen.blit(score1_text, (WIDTH - 300, 25))
    screen.blit(score2_text, (WIDTH - 300, 60))

def show_winner(winner):
    """Display the winner on the screen."""
    if winner == 0:
        winner_text = winner_font.render("It's a Tie!", True, (0, 0, 0))
    else:
        winner_text = winner_font.render(f"Player {winner} Wins!", True, (0, 0, 0))

    # Center the text horizontally and move it towards the center vertically
    text_rect = winner_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(winner_text, text_rect)

def show_game_over_screen(winner):
    """Display the game over screen with buttons."""
    game_over_font = pygame.font.Font('fonts/From Cartoon Blocks.ttf', 60)
    game_over_text = game_over_font.render("Game Over", True, (0, 0, 0))

    if winner == 0:
        result_text = game_over_font.render("It's a Tie!", True, (0, 0, 0))
    else:
        result_text = game_over_font.render(f"Player {winner} Wins!", True, (0, 0, 0))

    # Center the text horizontally and move it towards the center vertically
    game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    result_rect = result_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    play_again_button = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 50, 300, 50)
    quit_button = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 120, 300, 50)

    pygame.draw.rect(screen, (56, 70, 110), play_again_button)
    pygame.draw.rect(screen, (56, 70, 110), quit_button)

    play_again_text = score_font.render("Play Again", True, (0, 0, 0))
    quit_text = score_font.render("Quit", True, (0, 0, 0))

    # Center the text horizontally and move it towards the center vertically
    play_again_rect = play_again_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 80))
    quit_rect = quit_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))

    screen.blit(game_over_text, game_over_rect)
    screen.blit(result_text, result_rect)
    screen.blit(play_again_text, play_again_rect)
    screen.blit(quit_text, quit_rect)

    return play_again_button, quit_button

# Game loop
running = True
game_over = False

while running:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check for game over condition
    if game_over:
        play_again_button, quit_button = show_game_over_screen(1 if score1 > score2 else (2 if score2 > score1 else 0))

        # Update the display
        pygame.display.flip()

        # Check for button clicks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if play_again_button.collidepoint(mouse_pos):
                    # Restart the game
                    running = True
                    game_over = False
                    start_time = pygame.time.get_ticks()
                    score1 = 0
                    score2 = 0
                elif quit_button.collidepoint(mouse_pos):
                    # Quit the game
                    running = False

        # Skip plebe movement during game over screen
        continue

    # Player 1 controls
    if keys[pygame.K_RIGHT]:
        plebe1.velocity_x = 6
    elif keys[pygame.K_LEFT]:
        plebe1.velocity_x = -6
    else:
        plebe1.velocity_x = 0

    if keys[pygame.K_UP]:
        plebe1.jump(jump_sound)
    # Player 2 controls
    if keys[pygame.K_d]:
        plebe2.velocity_x = 6
    elif keys[pygame.K_a]:
        plebe2.velocity_x = -6
    else:
        plebe2.velocity_x = 0

    if keys[pygame.K_w]:
        plebe2.jump(jump_sound)

    # Check for collision with Herndon for Player 1
    if pygame.Rect.colliderect(cover1.rect, plebe1):
        current_time = pygame.time.get_ticks()
        if current_time - last_collision_time >= 1000:
            plebe1.rect.midbottom = herndon1.rect.midbottom
        if current_time - last_collision_time >= cooldown_duration:
            score1 += 1
            last_collision_time = current_time

    # Check for collision with Herndon for Player 2
    if pygame.Rect.colliderect(cover1.rect, plebe2):
        current_time = pygame.time.get_ticks()
        if current_time - last_collision_time >= 1000:
            plebe2.rect.midbottom = herndon1.rect.midbottom
        if current_time - last_collision_time >= cooldown_duration:
            score2 += 1
            last_collision_time = current_time

    # Update the position of Plebe and other game elements based on Plebe's movement
    plebe_group.update(screen, platform_group, herndon1)
    herndon_group.update()
    herndon1.update()
    cover_group.update()
    platform_group.update(screen, herndon1, plebe1)

    # Put background on the screen
    screen.blit(background, (0, 0))

    # Draw entities
    herndon_group.draw(screen)
    herndon1.draw(screen)

    # Draw a triangular obstacle above Herndon
    pygame.draw.polygon(
        screen,
        (150, 150, 150),
        [
            (herndon1.rect.midtop[0] - 150, herndon1.rect.top),
            (herndon1.rect.midtop[0], herndon1.rect.top - 100),
            (herndon1.rect.midtop[0] + 150, herndon1.rect.top),
        ],
    )

    platform_group.draw(screen)
    plebe_group.draw(screen)
    cover_group.draw(screen)

    # Show the timer and scores
    show_timer()
    show_scores()

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
