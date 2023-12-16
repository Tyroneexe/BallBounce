import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ball Bounce")

# Colors
white = (255, 255, 255)
red = (255, 0, 0)

# Set up the circle (ring)
outer_radius = 350
inner_radius = 330
circle_pos = (width // 2, height // 2)

# Set up the ball
ball_radius = 25
ball_pos = (width // 2, height // 2)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw the outer circle
    pygame.draw.circle(screen, white, circle_pos, outer_radius)

    # Draw the inner circle to create a ring
    pygame.draw.circle(screen, (0, 0, 0), circle_pos, inner_radius)

    # Draw the ball
    pygame.draw.circle(screen, red, ball_pos, ball_radius)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(30)
