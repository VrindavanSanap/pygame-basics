#!/usr/bin/python3

from math import cos, e, pi, sin, sqrt
from random import uniform

from pygame import *
from pygame.locals import *
from pygamehelper import *
from vec2d import *


class Starter(PygameHelper):
  def __init__(self):
    self.w, self.h = 800, 600
    PygameHelper.__init__(self, size=(self.w, self.h), fill=((255, 255, 255)))

    self.pos = vec2d(400, 300)
    self.target = vec2d(300, 300)

  def update(self):
    dir = self.target - self.pos
    if dir.length > 3:
      dir.length = 3
      self.pos += dir

  def keyDown(self, key):
    pass

  def keyUp(self, key):
    pass

  def mouseUp(self, button, pos):
    self.target = pos

  def mouseMotion(self, buttons, pos, rel):
    pass

  def draw(self):
    self.screen.fill((255, 255, 255))
    pygame.draw.circle(self.screen, (255, 0, 0), self.target, 30, 1)
    pygame.draw.circle(self.screen, (0, 0, 0), self.pos, 21, 1)
    pygame.draw.circle(self.screen, (200, 200, 255), self.pos, 20)


s = Starter()
s.mainLoop(40)
