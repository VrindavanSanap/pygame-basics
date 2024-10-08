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

  def update(self):
    pass

  def keyDown(self, key):
    pass

  def keyUp(self, key):
    pass

  def mouseUp(self, button, pos):
    pass

  def mouseMotion(self, buttons, pos, rel):
    pass

  def draw(self):
    r = uniform(0, 255)
    g = uniform(0, 255)
    b = uniform(0, 255)
    self.screen.fill((r, g, b))


s = Starter()
s.mainLoop(40)
