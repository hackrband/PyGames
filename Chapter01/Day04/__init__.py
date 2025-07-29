import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Drawing Shapes")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Main loop
def draw_shapes():
    screen.fill(WHITE)  # Fill the screen with white color

    # Draw circle
    pygame.draw.circle(screen, RED, (200, 150), 50)  # (x, y), radius

    # Draw triangle
    pygame.draw.polygon(screen, GREEN, [(400, 100), (300, 200), (500, 200)])

    # Draw square
    pygame.draw.rect(screen, BLUE, (100, 300, 100, 100))  # (x, y, width, height)

    # Draw pentagon
    def draw_pentagon(center, size):
        vertices = []
        for i in range(5):
            angle = math.radians(-90 + (360 / 5) * i)
            x = center[0] + size * math.cos(angle)
            y = center[1] + size * math.sin(angle)
            vertices.append((x, y))
        pygame.draw.polygon(screen, BLACK, vertices)

    draw_pentagon((400, 400), 50)

    pygame.display.flip()  # Update the display

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_shapes()

pygame.quit()
sys.exit()
