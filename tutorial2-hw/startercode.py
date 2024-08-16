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

  def update(self):
    pass

  def keyDown(self, key):
    pass

  def keyUp(self, key):
    pass

  def mouseUp(self, button, pos):
    # pygame.draw.circle(self.screen, (0,0,0), pos, 20)
    pass

  def mouseMotion(self, buttons, pos, rel):
    # buttons is tupple of mouse buttons
    # L M R

    if buttons[0] == 1:  ## if left mouse click draw
      offset = 35
      pygame.draw.line(
        self.screen,
        colors["black"],
        (pos[0], pos[1] + offset),
        (pos[0] - rel[0], pos[1] - rel[1] + offset),
        5,
      )
      pygame.draw.line(
        self.screen,
        colors["black"],
        (pos[0], pos[1] - offset),
        (pos[0] - rel[0], pos[1] - rel[1] - offset),
        5,
      )

    if buttons[2] == 1:  ## if right mouse click erase
      pygame.draw.circle(self.screen, colors["white"], pos, 25)

  def draw(self):
    pass


s = Starter()
s.mainLoop(40)
