import pyglet
from .igra import *
from .screen import *


class Object(pyglet.sprite.Sprite):
    def __init__(self, game, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vx = 0
        self.vy = 0
        self.tip = "Object"
        self.game = game

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

        if(window.height <= self.y):
            self.brisanje()
        if(self.y+self.height <= 0):
            self.brisanje()
            if(self.tip == 'Meteor'):
                self.game.dol += 1
                if(self.game.dol == 5):
                    self.game.dol = 0
                    self.game.score -= 70

    def brisanje(self):
        if(self.tip == 'Meteor'):
            try:
                self.game.meteorji_list.remove(self)
            except ValueError:
                pass

        if(self.tip == 'Metek'):
            try:
                self.game.metek_list.remove(self)
            except ValueError:
                pass
        if(self.tip == 'Powerup'):
            try:
                self.game.powerup_list.remove(self)
            except ValueError:
                pass
