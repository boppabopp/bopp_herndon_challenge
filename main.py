import pygame
from plebe1 import *
from helpers import make_background
from herndon import Herndon
from platforms import Platform
from cover import Cover
from pygame import mixer
from menu import *

pygame.init()

# Set width and height of screen
WIDTH = 1080
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Make the clock
clock = pygame.time.Clock()

# Make the background (only once)
background = make_background(screen)

# Give menu state a false value and game state a true value
MENU_STATE = 0
GAME_STATE = 1
game_state = MENU_STATE  # Initial state is the menu

# Create the Herndon sprite
herndon1 = Herndon(screen)
herndon_group = pygame.sprite.Group()
herndon_group.add(herndon1)

# Create the Plebe sprites for Player 1 and Player 2
plebe1 = Plebe(screen, pygame.image.load('images/plebe.png').convert_alpha(), 25, 0, herndon1.rect.centerx - 20)
plebe_group = pygame.sprite.Group()
plebe_group.add(plebe1)

plebe2 = Plebe(screen, pygame.image.load('images/plebe_g.png').convert_alpha(), 25, 0, + 20)
plebe_group.add(plebe2)


# Create the Cover sprite
cover1 = Cover(screen, herndon1, 20)
cover_group = pygame.sprite.Group()
cover_group.add(cover1)

# Create platforms dynamically
platform_group = pygame.sprite.Group()
for j in range(1, 6):  # 6 platforms
    random_y_i = (int((herndon1.rect.bottom - herndon1.rect.top) / 6))  # divides the height of herndon into 6 parts
    random_y = herndon1.rect.bottom - random_y_i * j  # puts each platforms at one of those parts
    platform = Platform(screen, random_y)  # makes an instance of each platform
    platform_group.add(platform)  # adds each platform to the group

# Initialize mixer and load audio files
mixer.init()
mixer.music.load('audio/music.oga')
mixer.music.play(-1)  # continuously loops the music
jump_sound = mixer.Sound('audio/jump.wav')  # make variable for jump sound

# Set up fonts for timer and score
timer_font = pygame.font.Font('fonts/From Cartoon Blocks.ttf', 40)
score_font = pygame.font.Font('fonts/From Cartoon Blocks.ttf', 35)

# Initialize how long the timer should count for
timer_sec = 60

# Initialize the game start time, last collision time, and end time
start_time = pygame.time.get_ticks()
last_collision_time = 0
end_time = 0

# Cooldown duration in milliseconds (adjust as needed)
cooldown_duration = 1000  # 1000 milliseconds = 1 second

# make an instance of the menu and set menu_displayed to true
#menu = Menu(screen)
menu_displayed = True


def show_timer():
    global timer_sec, game_over  # global means that any method/class can access it
    current_time = pygame.time.get_ticks()
    elapsed_seconds = (current_time - start_time) // 1000  # finds how much time has passed

    if elapsed_seconds < timer_sec:  # if it has not been 60 seconds, counts down from 60 seconds and shows it on screen
        timer_text = timer_font.render("00:%s" % str(timer_sec - elapsed_seconds), True, (0, 0, 0))
        screen.blit(timer_text, (50, 25))
    else:  # if it has been 60 seconds, the game over screen will show
        game_over = True


def show_scores():  # shows the scores in the top right of the screen
    score1_text = score_font.render("Player 1 Score: %d" % plebe1.score, True, (0, 0, 0))
    score2_text = score_font.render("Player 2 Score: %d" % plebe2.score, True, (0, 0, 0))
    screen.blit(score1_text, (WIDTH - 300, 25))
    screen.blit(score2_text, (WIDTH - 300, 60))

    # antialias just makes the words smoother looking


def show_game_over_screen(score1, score2):
    global game_over  # global variable means any method/class can access it
    game_over_font = pygame.font.Font('fonts/From Cartoon Blocks.ttf', 60)  # set font for all of this
    game_over_text = game_over_font.render("Game Over", True, (0, 0, 0))

    if score1 == score2 and game_over:  # if it's a tie
        result_text = game_over_font.render("It's a Tie!", True, (0, 0, 0))
    else:  # shows winner
        winner = 1 if score1 > score2 else 2
        result_text = game_over_font.render(f"Player {winner} Wins!", True, (0, 0, 0))

    game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))  # puts game over in correct place
    result_rect = result_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # puts result in correct place

    play_again_button = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 50, 300, 50)  # makes play again button
    quit_button = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 120, 300, 50)  # makes quit button

    pygame.draw.rect(screen, (56, 70, 110), play_again_button)
    pygame.draw.rect(screen, (56, 70, 110), quit_button)

    play_again_text = score_font.render("Play Again", True, (0, 0, 0))  # writes on the button
    quit_text = score_font.render("Quit", True, (0, 0, 0))

    play_again_rect = play_again_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 80))
    quit_rect = quit_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))

    # puts everything on the screen
    screen.blit(game_over_text, game_over_rect)
    screen.blit(result_text, result_rect)
    screen.blit(play_again_text, play_again_rect)
    screen.blit(quit_text, quit_rect)

    return play_again_button, quit_button


# Game loop, make running true and game over false
running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # provides way to exit game loop

    if menu_displayed:
        menu1 = Menu(screen)  # make instance of menu class
        menu1.display_menu()  # display it
        pygame.display.flip()

        for event in pygame.event.get():
            if menu1.handle_input(event):  # if the start button is clicked
                menu_displayed = False  # menu goes away
                start_time = pygame.time.get_ticks()  # initializes the start time
                plebe1.score = 0  # sets both of the scores to 0 (in case they were not 0 from previous game)
                plebe2.score = 0
                plebe1.rect.midbottom = (herndon1.rect.centerx - 20, herndon1.rect.bottom)  # resets plebe positions
                plebe2.rect.midbottom = (herndon1.rect.centerx + 20, herndon1.rect.bottom)
        pygame.display.flip()
    else:
        if game_over:  # if the timer runs out, shows the game over screen
            play_again_button, quit_button = show_game_over_screen(plebe1.score, plebe2.score)
            pygame.display.flip()

            # Check for button clicks
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos  # checks to see if the position of mouse should trigger an event
                    if play_again_button.collidepoint(mouse_pos):  # checks if mouse clicked on play again button
                        menu_displayed = True
                        game_over = False
                    elif quit_button.collidepoint(mouse_pos):  # checks if mouse clicked on quit button
                        running = False
            continue

        keys = pygame.key.get_pressed()  # sets variable for keys that were pressed

        # moves plebe left/right if holding left/right arrow keys down
        if keys[pygame.K_RIGHT]:
            plebe2.velocity_x = 6
        elif keys[pygame.K_LEFT]:
            plebe2.velocity_x = -6
        else:
            plebe2.velocity_x = 0
        # triggers jump method if up key is pressed
        if keys[pygame.K_UP]:
            plebe2.jump(jump_sound)

        # same as above code but for WAD keys
        if keys[pygame.K_d]:
            plebe1.velocity_x = 6
        elif keys[pygame.K_a]:
            plebe1.velocity_x = -6
        else:
            plebe1.velocity_x = 0

        if keys[pygame.K_w]:
            plebe1.jump(jump_sound)

        for plebe in plebe_group:  # check for if the plebe collide with the cover
            if plebe.check_collision(cover1):
                current_time = pygame.time.get_ticks()
                if current_time - last_collision_time >= 1000:  # provides slight buffer before sending them down
                    plebe.rect.midbottom = herndon1.rect.midbottom
                if current_time - last_collision_time >= cooldown_duration:  # provides cooldown for scoring
                    plebe.score += 1
                    last_collision_time = current_time  # resets last collision time

            if plebe.rect.right >= screen.get_width():  # does not allow plebes to move off of the screen (walls)
                plebe.rect.x = screen.get_width() - 50
            if plebe.rect.left <= 0:
                plebe.rect.x = 0

        # update all the groups
        plebe_group.update(screen, platform_group, herndon1)
        herndon_group.update()
        # herndon1.update()
        cover_group.update()
        platform_group.update(screen, herndon1, (plebe for plebe in plebe_group))

        screen.blit(background, (0, 0))

        # draw groups
        herndon_group.draw(screen)
        herndon1.draw(screen)

        # draw the triangle of herndon
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

        # show the timer and scores on the screen
        show_timer()
        show_scores()

        # Check for game over condition
        #if game_over:
            #play_again_button, quit_button = show_game_over_screen(plebe1.score, plebe2.score)
            #pygame.display.flip()

            # Check for button clicks
            #for event in pygame.event.get():
                #if event.type == pygame.QUIT:
                    #running = False
                #if event.type == pygame.MOUSEBUTTONDOWN:
                    #mouse_pos = event.pos
                    #if play_again_button.collidepoint(mouse_pos):
                        #menu_displayed = True
                        #game_over = False
                        #plebe1.rect.midbottom = herndon1.rect.midbottom
                        #plebe2.rect.midbottom = herndon1.rect.midbottom
                    #elif quit_button.collidepoint(mouse_pos):
                        #running = False

    clock.tick(60)  # set fps
    pygame.display.flip()

pygame.quit()
