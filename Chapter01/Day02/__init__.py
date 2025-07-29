# /Users/m.salim/PycharmProjects/Pygames/Chapter01/Day02/blue_car.gif
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Image Display")

image = pygame.image.load("/Users/m.salim/PycharmProjects/Pygames/Chapter01/Day02/blue_car.gif")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(image, (0, 0))

    pygame.display.flip()
