# import pyglet
from .import physObj
from . import gameover


class Powerup(physObj.PhysObj):
    def __init__(self, *args, power, **kwargs):
        super().__init__(*args, **kwargs)
        self.tip = "Powerup"
        self.power = power

    def power_fn(self):
        if(self.power == "xLife"):
            self.game.hp += 1
        if(self.power == "Bomb"):
            for m in self.game.meteorji_list:
                self.game.score += 20
                if(m.velikost == 'v'):
                    self.game.score += 10
            self.game.meteorji_list = []
        if(self.power == "Strel"):
            self.game.metki = True
            gameover.strel = True
            self.game.strel_timer = self.game.pu_timerbase
        if(self.power == "Speed"):
            self.game.raketa.vx = 300
            gameover.speed = True
            self.game.speed_timer = self.game.pu_timerbase
        if(self.power == "Hmetki"):
            self.game.raketa.timer_base = 1/3
            gameover.Hmetki = True
            self.game.Hmetki_timer = self.game.pu_timerbase
        if(self.power == "Freeze"):
            gameover.freeze = True
            self.game.freeze_timer = self.game.pu_timerbase
        if(self.power == "Shield"):
            gameover.shield = True
            self.game.shield_timer = self.game.pu_timerbase
        if(self.power == "Pmetki"):
            gameover.Pmetki = True
            self.game.Pmetki_timer = self.game.pu_timerbase
            self.game.raketa.timer_base = 2/3
        if(self.power == "slow"):
            self.game.raketa.vx = 100
            gameover.slow = True
            self.game.slow_timer = self.game.pu_timerbase
        if(self.power == "Hmeteorji"):
            for m in self.game.meteorji_list[:]:
                m.vy -= 70
            self.game.Hmeteorji_timer = self.game.pu_timerbase

    def zabij(self):
        self.power_fn()
        self.zabit = True
        self.brisanje()

    def collision(self, other):
        a = (self.width/2+other.width/2)**2
        b = (self.y+self.height/2-other.y-other.height/2)**2
        b += (self.x+self.width/2-other.x-other.width/2)**2
        if(a >= b):
            self.zabij()
