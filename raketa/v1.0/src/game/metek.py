from pyglet.window import key
import pyglet

from . import neMeteor


class Metek(neMeteor.NeMeteor):
    def __init__(self, game, *args, **kwargs):
        super().__init__(game, *args, **kwargs)
        self.vy = 400
        self.tip = "Metek"

    def brisanje(self):
        if(self.tip == 'Meteor'):
            self.game.game.meteorji_list.remove(self)
        if(self.tip == 'Metek'):
            self.game.game.metek_list.remove(self)
