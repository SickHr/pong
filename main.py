import pygame
import sys
from pygame.locals import *

# Constants for the game
WINDOW_WIDTH, WINDOW_HEIGHT = 640, 480
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 60
BALL_SIZE = 20
PADDLE_SPEED = 5
BALL_SPEED_X, BALL_SPEED_Y = 3, 2
WHITE = (255, 255, 255)

# Initialize Pygame
pygame.init()

# Set up the display
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pong Game")

# Set up the paddles and ball
paddle_a = pygame.Rect(10, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_b = pygame.Rect(WINDOW_WIDTH - 30, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WINDOW_WIDTH // 2 - BALL_SIZE // 2, WINDOW_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Set initial direction of the ball
ball_dir_x = BALL_SPEED_X
ball_dir_y = BALL_SPEED_Y

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[K_w]:
        paddle_a.move_ip(0, -PADDLE_SPEED)
    if keys[K_s]:
        paddle_a.move_ip(0, PADDLE_SPEED)
    if keys[K_UP]:
        paddle_b.move_ip(0, -PADDLE_SPEED)
    if keys[K_DOWN]:
        paddle_b.move_ip(0, PADDLE_SPEED)

    # Move the ball
    ball.move_ip(ball_dir_x, ball_dir_y)

    # Collision detection
    if ball.top <= 0 or ball.bottom >= WINDOW_HEIGHT:
        ball_dir_y = -ball_dir_y
    if ball.colliderect(paddle_a) or ball.colliderect(paddle_b):
        ball_dir_x = -ball_dir_x
    if ball.left <= 0 or ball.right >= WINDOW_WIDTH:
        ball.x = WINDOW_WIDTH // 2 - BALL_SIZE // 2
        ball.y = WINDOW_HEIGHT // 2 - BALL_SIZE // 2
        ball_dir_x = BALL_SPEED_X

    # Clear screen
    window.fill((0, 0, 0))

    # Draw paddles and ball
    pygame.draw.rect(window, WHITE, paddle_a)
    pygame.draw.rect(window, WHITE, paddle_b)
    pygame.draw.ellipse(window, WHITE, ball)
    pygame.draw.aaline(window, WHITE, (WINDOW_WIDTH // 2, 0), (WINDOW_WIDTH // 2, WINDOW_HEIGHT))

    # Update display
    pygame.display.update()

    # Frame Per Second / Refresh Rate
    pygame.time.Clock().tick(60)