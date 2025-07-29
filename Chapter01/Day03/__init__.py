import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moving Block")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

block_width = 50
block_height = 50
block_x = (SCREEN_WIDTH - block_width) // 2
block_y = (SCREEN_HEIGHT - block_height) // 2
block_speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                block_x -= block_speed
            elif event.key == pygame.K_RIGHT:
                block_x += block_speed
            elif event.key == pygame.K_UP:
                block_y -= block_speed
            elif event.key == pygame.K_DOWN:
                block_y += block_speed

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, (block_x, block_y, block_width, block_height))

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
