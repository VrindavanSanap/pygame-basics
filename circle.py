#!/usr/bin/python3


import sys

import pygame

pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Circle Drawing Example")

# Colors
white = (255, 255, 255)
red = (255, 0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)

    # Draw a red filled circle at the center of the screen
    circle_center = (0, 0)
    circle_radius = 50
    pygame.draw.circle(screen, red, circle_center, circle_radius)

    # Draw a red hollow circle at the center of the screen
    circle_center = (width * 2 // 3, height // 2)
    circle_radius = 50
    circle_width = 2
    pygame.draw.circle(screen, red, circle_center, circle_radius, circle_width)

    pygame.display.flip()

pygame.quit()
sys.exit()
