# import pyglet
from pyglet.window import key
from .seznami import *
from . import neMeteor, metek
from .screen import *
from . import gameover
from . import resources


class Raketa(neMeteor.NeMeteor):
    def __init__(self, game, *args, **kwargs):
        super().__init__(game, *args, **kwargs)
        self.key_handler = key.KeyStateHandler()
        self.x = 500//2-self.width//2
        self.vx = 200
        self.scale = 0.992
        self.timer = 0
        self.timer_base = 1/5

        self.tip = 'Raketa'

    def update(self, dt):
        self.timer -= dt
        # self.vx *= self.scale
        if(self.key_handler[key.LEFT]):
            self.x -= self.vx*dt
        if(self.key_handler[key.RIGHT]):
            self.x += self.vx*dt
        if(self.x <= -self.width//2):
            self.x = 500-self.width//2
        if(self.x > 500-self.width//2):
            self.x = -self.width//2
        if(self.key_handler[key.SPACE]):
            if(self.timer <= 0):
                self.strel()
                self.timer = self.timer_base*self.scale
        if(self.key_handler[key.P]):
                gameover.pause = True
                for i in self.game.menuPause.buttons[:]:
                    i.hover = False
                    self.game.menuPause.sprememba = True
                self.game.mouse_motion(250, 300, 0, 0)

    def collision(self, other):
        super().collision(other)

    def strel(self):
        tmp = metek.Metek(
            self,
            self.game.slika_metek,
            batch=self.game.main_batch,
            )
        if(self.game.metki):
            tmp.x = self.x + self.width//3-2
            tmp.y = self.height
            self.game.metek_list.append(tmp)
            tmp = metek.Metek(
                self,
                resources.bull1,
                batch=self.game.main_batch
            )
            tmp.x = self.x + 2*self.width//3-2
            tmp.y = self.height
            self.game.metek_list.append(tmp)
        else:
            tmp.x = self.x + self.width//2-2
            tmp.y = self.height
            self.game.metek_list.append(tmp)

    def life(self):
        if(self.game.hp == 0):
            self.brisanje()
            self.zabit = True
            gameover.game_over = True
            self.game.highScores.enterName()
            for i in self.game.menuPause.buttons[:]:
                i.hover = False
                self.game.menuPause.sprememba = True
            self.game.mouse_motion(250, 300, 0, 0)
        else:
            self.zabit = True
            self.game.hp -= 1
        self.game.meteorji_list = []
        self.game.metek_list = []
        self.game.powerup_list = []
