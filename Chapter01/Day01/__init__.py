import pygame
import sys

pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hello Pygames")

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update game state and draw to the screen
    pygame.display.flip()

    # Sample code snippet for displaying text in a Pygame window
    font = pygame.font.Font(None, 36)
    text = font.render("Hello, Pygame!", True, (255, 255, 255))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Draw "Hello, Pygame!" on the screen
        screen.fill((0, 0, 0))
        screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))

        # Update the display