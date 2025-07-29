import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Image Display")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    try:
        address = input("Input the address of the image: ")
        image = pygame.image.load(address)
    except pygame.error:
        print("Error: Failed to load image. Please check the address and try again.")
        continue  # Continue to the next iteration of the loop

    screen.blit(image, (0, 0))

    pygame.display.flip()
