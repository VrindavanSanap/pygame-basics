#!/usr/bin/python3

from pygamehelper import *
from pygame import *
from pygame.locals import *
from vec2d import *
from math import e, pi, cos, sin, sqrt
from random import uniform


colors = {
    "black": (0, 0, 0), 
    "white": (255, 255, 255)
}


class Starter(PygameHelper):
    def __init__(self):
        self.w, self.h = 800, 600
        PygameHelper.__init__(self, size=(self.w, self.h), fill=((255,255,255)))

    def update(self):
        pass

    def keyDown(self, key):
        pass 

    def keyUp(self, key):
        pass

    def mouseUp(self, button, pos):
        #pygame.draw.circle(self.screen, (0,0,0), pos, 20)        
        pass
        
    def mouseMotion(self, buttons, pos, rel):
        # buttons is tupple of mouse buttons 
        # L M R 

        if buttons[0] == 1: ## if left mouse click draw
            pygame.draw.line(self.screen ,colors["black"] ,pos ,(pos[0] - rel[0], pos[1] - rel[1]), 5)        
 
        if buttons[2] == 1: ## if right mouse click erase 
            pygame.draw.circle(self.screen ,colors["white"], pos, 25) 

    def draw(self):
        pass


s = Starter()
s.mainLoop(40)