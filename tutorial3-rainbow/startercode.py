#!/usr/bin/python3

from math import cos, e, pi, sin, sqrt
from random import uniform

from pygame import *
from pygame.locals import *
from pygamehelper import *
from vec2d import *

colors = {"black": (0, 0, 0), "white": (255, 255, 255)}


class Starter(PygameHelper):
    def __init__(self):
        self.w, self.h = 800, 600
        PygameHelper.__init__(self, size=(self.w, self.h), fill=((255, 255, 255)))
        img = pygame.image.load("colors.png")
        self.screen.blit(img, (0, 0))
        self.drawcolor = colors["black"]
        self.rainbow_mode = True
        self.x = 0

    def update(self):
        pass

    def keyDown(self, key):
        pass

    def keyUp(self, key):
        pass

    def mouseUp(self, button, pos):
        pass

    def mouseMotion(self, buttons, pos, rel):
        # buttons is tupple of mouse buttons
        # L M R

        if pos[0] >= 172 + 25 or pos[1] >= 172 + 25:
            if buttons[0] == 1:  ## if left mouse click draw
                if self.rainbow_mode == True:
                    self.x += 1
                    if self.x >= 172:
                        self.x = 0
                    self.drawcolor = self.screen.get_at((self.x, 0))
                    print(f"coords:{pos[0], pos[1]}, color {self.drawcolor}")
                pygame.draw.line(
                    self.screen,
                    self.drawcolor,
                    pos,
                    (pos[0] - rel[0], pos[1] - rel[1]),
                    5,
                )

            elif buttons[2] == 1:  ## if right mouse click erase
                pygame.draw.circle(self.screen, colors["white"], pos, 25)

        else:
            if buttons[0] == 1:
                self.drawcolor = self.screen.get_at(pos)
                pygame.draw.circle(self.screen, self.drawcolor, (300, 100), 30)

    def draw(self):
        pass


s = Starter()
s.mainLoop(40)
