import pyglet
from .screen import *
from .gameover import *
from . import gumb

from game import resources


class Menu():
    def __init__(self, hover=resources.GNp, no_hover=resources.GN):
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
        self.buttonsBatch.draw()

    def preveriKlike(self, x, y):
        for i in self.buttons:
            i.klik(x, y)

    def checkHover(self):
        for i in self.buttons[:]:
            """# ce gres z misko cez se spremeni
            if(i.name == 'Choose1'):
                # preveri ce je slika prava, drugace zamenja
                if(i.hover):
                    i.image = self.GchooseB
                else:
                    i.image = self.GchooseB1
            elif(i.name == 'Choose2'):
                if(i.hover):
                    i.image = self.GchooseS
                else:
                    i.image = self.GchooseS1
            else:"""
            if(i.hover):
                i.image = self.hover
            else:
                i.image = self.no_hover

    def addButton(self):
        pass
