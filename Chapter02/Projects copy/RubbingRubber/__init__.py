import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moving Image")

BACKGROUND_COLOR = (136, 136, 136)  # RGB values for #888888

# Load the image
image = pygame.image.load('/Users/m.salim/PycharmProjects/Pygames/Projects/RubbingRubber/blue_car.gif')  # Replace with the path to your image
original_width, original_height = image.get_size()

# Calculate scaling factors to make the image 50% smaller
scale_factor = 0.5  # 50% smaller

# Scale the image
image = pygame.transform.scale(image, (int(original_width * scale_factor), int(original_height * scale_factor)))

# Rotate the image
image = pygame.transform.rotate(image, -90)  # Rotate 90 degrees upward

image_rect = image.get_rect()
image_rect.center = (SCREEN_HEIGHT // 2, SCREEN_HEIGHT // 2)
block_speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                image_rect.x -= block_speed
            elif event.key == pygame.K_RIGHT:
                image_rect.x += block_speed
            elif event.key == pygame.K_UP:
                image_rect.y -= block_speed
            elif event.key == pygame.K_DOWN:
                image_rect.y += block_speed

    screen.fill(BACKGROUND_COLOR)  # Set background color

    # Blit the image onto the screen
    screen.blit(image, image_rect)

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
