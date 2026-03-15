import pygame
import random
# Initialize Pygame
pygame.init()
# Set up the game window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Screen with Sprites")
# Define colors
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
# Define the player sprite (black rectangle)
player_size = (50, 30)
player_pos = [WIDTH // 2, HEIGHT // 2]
# Define the random sprite (blue square)
random_size = (30, 30)
random_pos = [random.randint(0, WIDTH - random_size[0]), random.randint(0, HEIGHT - random_size[1])]
# Game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5
    if keys[pygame.K_UP]:
        player_pos[1] -= 5
    if keys[pygame.K_DOWN]:
        player_pos[1] += 5
    # Move the random sprite randomly
    random_pos[0] += random.choice([-5, 0, 5])
    random_pos[1] += random.choice([-5, 0, 5])
    # Fill the background
    screen.fill((255, 255, 255))
    # Draw the sprites
    pygame.draw.rect(screen, BLACK, (*player_pos, *player_size))
    pygame.draw.rect(screen, BLUE, (*random_pos, *random_size))
    # Update the display
    pygame.display.flip()
    clock.tick(30)