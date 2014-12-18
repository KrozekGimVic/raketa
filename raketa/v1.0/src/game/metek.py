import pyglet
from pyglet.window import key
from . import neMeteor

class Metek(neMeteor.NeMeteor):
    def __init__ (self, game, *args,**kwargs):
        super().__init__(game, *args, **kwargs)
        self.vy = 400
        self.tip = "Metek"

    def brisanje(self):
       # print("brisem se!!!!")
        if(self.tip=='Meteor'):
            #print(meteorji_list)
            self.game.game.meteorji_list.remove(self)
        if(self.tip=='Metek'):
            self.game.game.metek_list.remove(self)
