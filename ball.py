import pygame
import sys
import math

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

# Set up the circle (ring)
outer_radius = 350
inner_radius = 330
circle_pos = (width // 2, height // 2)

# Set up the ball
ball_radius = 25
ball_pos = [width // 2, height // 2]
ball_velocity = [5, 5]  # Initial velocity of the ball

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
        ball_velocity[0] = -ball_velocity[0]
        if ball_pos[0] - ball_radius < 0:
            ball_pos[0] = ball_radius
        else:
            ball_pos[0] = width - ball_radius

    if ball_pos[1] - ball_radius < 0 or ball_pos[1] + ball_radius > height:
        ball_velocity[1] = -ball_velocity[1]
        if ball_pos[1] - ball_radius < 0:
            ball_pos[1] = ball_radius
        else:
            ball_pos[1] = height - ball_radius

    # Check for collision with the ring
    distance = math.sqrt((ball_pos[0] - circle_pos[0]) ** 2 + (ball_pos[1] - circle_pos[1]) ** 2)
    if inner_radius <= distance <= outer_radius:
        # Reverse the velocity to bounce off the ring
        ball_velocity[0] = -ball_velocity[0]
        ball_velocity[1] = -ball_velocity[1]

    # Clear the screen
    screen.fill(background_color)

    # Draw the outer circle
    pygame.draw.circle(screen, white, circle_pos, outer_radius)

    # Draw the inner circle to create a ring
    pygame.draw.circle(screen, background_color, circle_pos, inner_radius)

    # Draw the ball
    pygame.draw.circle(screen, red, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(30)
