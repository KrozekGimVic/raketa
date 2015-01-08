import pyglet
from .screen import *
from .gameover import *
from . import gumb

from game import resources


class Menu():
    def __init__(self, hover=resources.GNp, no_hover=resources.GN):
        #gameover.game_over=True
        #gumb=gumb.Gumb
        self.buttons = []
        self.buttonsBatch = pyglet.graphics.Batch()
        self.labels = []

        self.sprememba = False
        self.hover = hover
        self.no_hover = no_hover

    def draw(self):
        if(self.sprememba):
            self.checkHover()
            self.sprememba = False
        #self.buttonsBatch.draw()
        #print(self.buttons)
##        for i in self.buttons[:]:
##            if(self.game.hover==True):
##                tmp = pyglet.sprite.Sprite(resources.GNp, x = i.x, y = i.y)
##                tmp.anchor_x = tmp.width/2
##                tmp.anchor_y = tmp.height/2
##                tmp.draw()
##            else:
##                i.draw()
        self.buttonsBatch.draw()

    def preveriKlike(self, x, y):
        #print("preverjam")
        for i in self.buttons:
            i.klik(x, y)

    def checkHover(self):
        for i in self.buttons[:]:
            if(i.hover is True):
                #import pdb; pdb.set_trace()
                i.image = self.hover
                #preveri ce je slika prava, drugace zamenjaj
            else:
                i.image = self.no_hover
                #preveri ce je slika prava, drugace zamenjaj

    def addButton(self):
        pass









