import pygame
import sys
import os
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()
# Define constants for the screen width and height
screen = pygame.display.set_mode((600, 480))
bg = pygame.image.load(os.path.join("./", "back.png"))
pygame.mouse.set_visible(0)
pygame.display.set_caption('Garden Game')

while True:
    clock.tick(60)

    screen.blit(bg, (0, 0))

    x, y = pygame.mouse.get_pos()


    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            sys.exit()
    pygame.display.update()
