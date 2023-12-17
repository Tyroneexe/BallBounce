import pygame
import sys
import play_sound #as play_sound
import threading

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ball Bounce")

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
background_color = (0, 0, 0)  # Change this to your desired background color

# Set up the ball
ball_radius = 25
ball_pos = [width // 2, height // 2]
ball_velocity = [3, 3.4]  # Initial velocity of the ball
current_note_index = 0

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the ball position
    ball_pos[0] += ball_velocity[0]
    ball_pos[1] += ball_velocity[1]

    # Bounce the ball off the walls
    if ball_pos[0] - ball_radius < 0 or ball_pos[0] + ball_radius > width:
        ball_velocity[0] = -ball_velocity[0] - 1.2
        if ball_pos[0] - ball_radius < 0:
            ball_pos[0] = ball_radius
        else:
            ball_pos[0] = width - ball_radius
            
            ball_radius += 2
            
            ball_velocity[0] *= 1.09
            
            # Play the current note from the theme_song list
            play_sound.play_note(*play_sound.theme_song[current_note_index])

            # Move to the next note in the theme_song list
            current_note_index = (current_note_index + 1) % len(play_sound.theme_song)

    if ball_pos[1] - ball_radius < 0 or ball_pos[1] + ball_radius > height:
        ball_velocity[1] = -ball_velocity[1] + 1.2
        if ball_pos[1] - ball_radius < 0:
            ball_pos[1] = ball_radius
        else:
            ball_pos[1] = height - ball_radius
            
            ball_radius += 2
            
            ball_velocity[1] *= 1.09
            
            # Play the current note from the theme_song list
            play_sound.play_note(*play_sound.theme_song[current_note_index])

            # Move to the next note in the theme_song list
            current_note_index = (current_note_index + 1) % len(play_sound.theme_song)

    # Clear the screen
    screen.fill(background_color)

    # Draw the ball
    pygame.draw.circle(screen, red, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(100)
