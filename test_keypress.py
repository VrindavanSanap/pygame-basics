#!/usr/bin/python3

import pygame
import sys

pygame.init()

screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Key Press Example")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_q]:
            print("'q' key is pressed!")

        if keys[pygame.K_w]:
            print("'w' key is pressed!")
          
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(60)

