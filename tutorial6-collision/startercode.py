#!/usr/bin/python3

from math import cos, e, pi, sin, sqrt
from random import uniform

from pygame import *
from pygame.locals import *
from pygamehelper import *
from vec2d import *


class Agent:
  def __init__(self):
    self.pos = vec2d(0, 0)
    self.target = vec2d(0, 0)


class Starter(PygameHelper):
  def __init__(self):
    self.w, self.h = 800, 600
    PygameHelper.__init__(self, size=(self.w, self.h), fill=((255, 255, 255)))
    self.agents = []
    for i in range(10):
      a = Agent()
      a.pos = vec2d(uniform(0, self.w), uniform(0, self.h))
      a.target = vec2d(uniform(0, self.w), uniform(0, self.h))
      self.agents.append(a)

    self.selected = self.agents[0]

  def update(self):
    global c
    for a in self.agents:
      dir = a.target - a.pos
      if dir.length > 3:
        dir.length = 3
        a.pos += dir
    for a1 in self.agents:
      for a2 in self.agents:
        if a1 == a2:
          continue
        dist = a1.pos.get_distance(a2.pos)
        if dist < 40:
          overlap = 40 - dist
          direction = a2.pos - a1.pos
          direction.length = overlap
          if a1 == self.selected:
            a2.pos += direction
          elif a2 == self.selected:
            a1.pos -= direction
          else:
            direction.length = overlap / 2
            a2.pos += direction
            a1.pos -= direction

  def keyDown(self, key):
    pass

  def keyUp(self, key):
    pass

  def mouseUp(self, button, pos):
    if button == 3:
      self.selected.target = vec2d(pos)

    if button == 1:
      for agent in self.agents:
        dist = agent.pos.get_distance(pos)
        if dist < 20:
          self.selected = agent

  def mouseMotion(self, buttons, pos, rel):
    pass

  def draw(self):
    self.screen.fill((255, 255, 255))
    for a in self.agents:
      if not a == self.selected:
        pygame.draw.circle(self.screen, (255, 0, 0), a.target, 30, 1)
        pygame.draw.circle(self.screen, (0, 0, 0), a.pos, 21, 1)
        pygame.draw.circle(self.screen, (200, 200, 255), a.pos, 20)
      else:
        pygame.draw.circle(self.screen, (255, 0, 0), a.target, 30, 1)
        pygame.draw.circle(self.screen, (0, 0, 0), a.pos, 21, 1)
        pygame.draw.circle(self.screen, (200, 100, 255), a.pos, 20)


s = Starter()
s.mainLoop(40)
